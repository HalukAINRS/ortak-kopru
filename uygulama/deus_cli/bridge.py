"""Yerel kullanıcı yüzeyi ile açık CLI oturumları arasında kalıcı istek/yanıt köprüsü."""
import argparse
import contextlib
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import sqlite3
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlsplit
import uuid


class Conflict(ValueError):
    pass


def now():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def words(value):
    if not isinstance(value, str) or not value.strip() or len(value) > 250000:
        raise ValueError('Boş olmayan, en çok 250000 karakterlik metin gerekli.')
    return value  # Özgün boşluklar ve satır sonları korunur.


@contextlib.contextmanager
def process_lock(path):
    # WinPE'de SQLite kilitleri tek başına eşzamanlı alımı ayırmadı.
    if os.name == 'nt':
        import ctypes
        api = ctypes.WinDLL('kernel32', use_last_error=True)
        api.CreateMutexW.argtypes = [ctypes.c_void_p,ctypes.c_int,ctypes.c_wchar_p]
        api.CreateMutexW.restype = ctypes.c_void_p
        api.WaitForSingleObject.argtypes = [ctypes.c_void_p,ctypes.c_ulong]
        api.ReleaseMutex.argtypes = [ctypes.c_void_p]
        api.CloseHandle.argtypes = [ctypes.c_void_p]
        name = 'Local\\HalukAI.DeusBridge.'+hashlib.sha256(str(path).casefold().encode()).hexdigest()
        handle = api.CreateMutexW(None,False,name)
        if not handle:
            raise ctypes.WinError(ctypes.get_last_error())
        acquired = False
        try:
            result = api.WaitForSingleObject(handle,10000)
            if result not in (0,128):
                raise TimeoutError('Köprüde başka bir yazıcı var; yeniden dene.')
            acquired = True
            yield
        finally:
            if acquired: api.ReleaseMutex(handle)
            api.CloseHandle(handle)
    else:
        import fcntl
        with Path(str(path)+'.lock').open('a+b') as stream:
            fcntl.flock(stream,fcntl.LOCK_EX)
            try:
                yield
            finally:
                fcntl.flock(stream,fcntl.LOCK_UN)


class Store:
    def __init__(self, directory):
        self.directory = Path(directory).resolve()
        self.directory.mkdir(parents=True, exist_ok=True)
        self.path = self.directory / 'bridge.sqlite3'
        with self.db() as db:
            db.executescript('''
                CREATE TABLE IF NOT EXISTS sessions (
                    id TEXT PRIMARY KEY, participant TEXT NOT NULL, label TEXT NOT NULL,
                    registered TEXT NOT NULL, last_seen TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS jobs (
                    id TEXT PRIMARY KEY, session_id TEXT NOT NULL REFERENCES sessions(id),
                    created TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS turns (
                    job_id TEXT NOT NULL REFERENCES jobs(id), revision INTEGER NOT NULL,
                    request_key TEXT NOT NULL UNIQUE, original_words TEXT NOT NULL,
                    source_note TEXT NOT NULL, created TEXT NOT NULL,
                    status TEXT NOT NULL CHECK(status IN ('queued','claimed','answered')),
                    claimed_at TEXT, response TEXT, sources TEXT, answered_at TEXT,
                    PRIMARY KEY(job_id,revision));
                CREATE TABLE IF NOT EXISTS events (
                    seq INTEGER PRIMARY KEY AUTOINCREMENT, job_id TEXT NOT NULL,
                    revision INTEGER NOT NULL, kind TEXT NOT NULL, at TEXT NOT NULL);
            ''')

    @contextlib.contextmanager
    def db(self):
        with process_lock(self.path):
            db = sqlite3.connect(self.path, timeout=10)
            try:
                db.row_factory = sqlite3.Row
                db.execute('PRAGMA foreign_keys=ON')
                with db:
                    yield db
            finally:
                db.close()

    @staticmethod
    def event(db, job, revision, kind):
        db.execute('INSERT INTO events(job_id,revision,kind,at) VALUES(?,?,?,?)',
                   (job, revision, kind, now()))

    @staticmethod
    def session_id(participant, external_session):
        return hashlib.sha256((participant+'\0'+external_session).encode()).hexdigest()

    def connect(self, participant, external_session, label):
        participant, external_session, label = map(words, (participant, external_session, label))
        session = self.session_id(participant, external_session)
        with self.db() as db:
            db.execute('''INSERT INTO sessions VALUES(?,?,?,?,?) ON CONFLICT(id)
                DO UPDATE SET label=excluded.label,last_seen=excluded.last_seen''',
                       (session, participant, label, now(), now()))
        return {'session_id': session, 'participant': participant, 'label': label,
                'identity_basis': 'local_cli_registration', 'identity_verified': False}

    def submit(self, session, text, request_key, source_note='', job_id=None):
        text, request_key = words(text), words(request_key)
        if len(request_key) > 160 or not isinstance(source_note, str):
            raise ValueError('Geçersiz istek anahtarı veya kaynak notu.')
        with self.db() as db:
            db.execute('BEGIN IMMEDIATE')
            existing = db.execute('SELECT * FROM turns WHERE request_key=?', (request_key,)).fetchone()
            if existing:
                target = db.execute('SELECT session_id FROM jobs WHERE id=?', (existing['job_id'],)).fetchone()
                if (existing['original_words'] != text or target['session_id'] != session
                        or existing['source_note'] != source_note
                        or (job_id is not None and existing['job_id'] != job_id)):
                    raise Conflict('Bu istek anahtarı başka bir içerikle kullanılmış.')
                return self.job(existing['job_id'], db)
            if not db.execute('SELECT id FROM sessions WHERE id=?', (session,)).fetchone():
                raise ValueError('Hedef CLI oturumu kayıtlı değil.')
            if job_id:
                job = db.execute('SELECT * FROM jobs WHERE id=?', (job_id,)).fetchone()
                if not job or job['session_id'] != session:
                    raise Conflict('Düzeltme aynı işe ve aynı CLI oturumuna bağlı olmalı.')
                revision = db.execute('SELECT MAX(revision)+1 FROM turns WHERE job_id=?', (job_id,)).fetchone()[0]
            else:
                job_id, revision = uuid.uuid4().hex, 1
                db.execute('INSERT INTO jobs VALUES(?,?,?)', (job_id, session, now()))
            db.execute('''INSERT INTO turns(job_id,revision,request_key,original_words,
                source_note,created,status) VALUES(?,?,?,?,?,?,'queued')''',
                       (job_id, revision, request_key, text, source_note, now()))
            self.event(db, job_id, revision, 'submitted')
            return self.job(job_id, db)

    def job(self, job_id, db=None):
        if db is None:
            with self.db() as connection:
                return self.job(job_id, connection)
        row = db.execute('''SELECT j.*,s.participant,s.label FROM jobs j JOIN sessions s
                            ON j.session_id=s.id WHERE j.id=?''', (job_id,)).fetchone()
        if not row:
            raise ValueError('İş bulunamadı.')
        result = dict(row)
        result['turns'] = []
        for turn in db.execute('SELECT * FROM turns WHERE job_id=? ORDER BY revision', (job_id,)):
            item = dict(turn)
            item['sources'] = json.loads(item['sources'] or '[]')
            item['input_sha256'] = hashlib.sha256(item['original_words'].encode()).hexdigest()
            result['turns'].append(item)
        return result

    def state(self):
        with self.db() as db:
            return {'application': 'deus_ex_machina', 'protocol': 1,
                    'sessions': [dict(r) for r in db.execute('SELECT * FROM sessions ORDER BY registered')],
                    'jobs': [self.job(r[0], db) for r in db.execute('SELECT id FROM jobs ORDER BY created DESC LIMIT 50')]}

    def receive(self, session):
        with self.db() as db:
            db.execute('BEGIN IMMEDIATE')
            if not db.execute('SELECT id FROM sessions WHERE id=?', (session,)).fetchone():
                raise ValueError('Önce bu CLI oturumunu connect ile kaydet.')
            db.execute('UPDATE sessions SET last_seen=? WHERE id=?', (now(), session))
            row = db.execute('''SELECT t.* FROM turns t JOIN jobs j ON j.id=t.job_id
                WHERE j.session_id=? AND t.status='claimed' ORDER BY t.claimed_at LIMIT 1''', (session,)).fetchone()
            redelivered = row is not None
            if row is None:
                row = db.execute('''SELECT t.* FROM turns t JOIN jobs j ON j.id=t.job_id
                    WHERE j.session_id=? AND t.status='queued' ORDER BY t.created LIMIT 1''', (session,)).fetchone()
                if row is None:
                    return {'request': None}
                db.execute("UPDATE turns SET status='claimed',claimed_at=? WHERE job_id=? AND revision=?",
                           (now(), row['job_id'], row['revision']))
                self.event(db, row['job_id'], row['revision'], 'cli_received')
            result = self.job(row['job_id'], db)
            result['revision'] = row['revision']
            result['redelivered'] = redelivered
            return {'request': result}

    def reply(self, session, job_id, revision, response, source_paths):
        response = words(response)
        sources = []
        for source in source_paths:
            path = Path(source).resolve(strict=True)
            data = path.read_bytes()
            sources.append({'path': str(path), 'name': path.name, 'bytes': len(data),
                            'sha256': hashlib.sha256(data).hexdigest(),
                            'observation': 'bytes_read_by_cli_reply_command'})
        encoded = json.dumps(sources, ensure_ascii=False, sort_keys=True)
        with self.db() as db:
            db.execute('BEGIN IMMEDIATE')
            job = self.job(job_id, db)
            if job['session_id'] != session:
                raise Conflict('Yanıt seçilen CLI oturumundan gelmeli.')
            row = db.execute('SELECT * FROM turns WHERE job_id=? AND revision=?', (job_id, revision)).fetchone()
            if not row:
                raise ValueError('İşin bu sürümü yok.')
            if row['status'] == 'answered':
                if row['response'] != response or row['sources'] != encoded:
                    raise Conflict('Yanıt değiştirilmez; aynı işe yeni bir düzeltme iletisi ekle.')
                return job
            if row['status'] != 'claimed':
                raise Conflict('İstek bu CLI tarafından henüz alınmadı.')
            db.execute("UPDATE turns SET status='answered',response=?,sources=?,answered_at=? WHERE job_id=? AND revision=?",
                       (response, encoded, now(), job_id, revision))
            self.event(db, job_id, revision, 'cli_replied')
            db.execute('UPDATE sessions SET last_seen=? WHERE id=?', (now(), session))
            return self.job(job_id, db)


def handler(store):
    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *_):
            pass  # Özgün girdiler HTTP erişim günlüğüne yazılmaz.

        def allowed(self):
            valid = {f'{self.server.server_address[0]}:{self.server.server_port}', f'localhost:{self.server.server_port}'}
            host = self.headers.get('Host', '')
            origin = self.headers.get('Origin')
            return host in valid and (origin is None or origin == 'http://'+host)

        def send(self, status, value, kind='application/json; charset=utf-8'):
            body = value if isinstance(value, bytes) else json.dumps(value, ensure_ascii=False).encode()
            self.send_response(status)
            self.send_header('Content-Type', kind)
            self.send_header('Content-Length', str(len(body)))
            self.send_header('Cache-Control', 'no-store')
            self.send_header('X-Content-Type-Options', 'nosniff')
            self.send_header('Content-Security-Policy', "default-src 'self'; script-src 'self'; style-src 'self'; connect-src 'self'; frame-ancestors 'none'")
            self.end_headers()
            self.wfile.write(body)

        def do_GET(self):
            if not self.allowed():
                return self.send(403, {'error': 'Yerel arayüz adresi gerekli.'})
            path = urlsplit(self.path).path
            if path == '/api/state':
                return self.send(200, store.state())
            resources = {'/': ('index.html','text/html; charset=utf-8'),
                         '/app.js': ('app.js','application/javascript; charset=utf-8'),
                         '/style.css': ('style.css','text/css; charset=utf-8')}
            if path in resources:
                name, kind = resources[path]
                return self.send(200, Path(__file__).with_name(name).read_bytes(), kind)
            return self.send(404, {'error': 'Bulunamadı.'})

        def do_POST(self):
            if not self.allowed():
                return self.send(403, {'error': 'Yerel arayüz adresi gerekli.'})
            if self.path != '/api/messages':
                return self.send(404, {'error': 'Bulunamadı.'})
            try:
                size = int(self.headers.get('Content-Length', '0'))
                if not 0 < size <= 1100000 or self.headers.get_content_type() != 'application/json':
                    raise ValueError('JSON gövdesi gerekli; en çok 1.1 MB.')
                data = json.loads(self.rfile.read(size))
                if not isinstance(data, dict):
                    raise ValueError('JSON nesnesi gerekli.')
                job = store.submit(data['session_id'], data['words'], data['request_key'],
                                   data.get('source_note','Kullanıcı arayüzünden gönderildi.'), data.get('job_id'))
                return self.send(200, job)
            except Conflict as error:
                return self.send(409, {'error': str(error)})
            except (ValueError, KeyError, TypeError) as error:
                return self.send(400, {'error': str(error)})
    return Handler


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--state-dir', required=True, help='Kalıcı özel dizin; Git deposunun dışında tut.')
    commands = parser.add_subparsers(dest='command', required=True)
    serve = commands.add_parser('serve')
    serve.add_argument('--port', type=int, default=8765)
    connect = commands.add_parser('connect')
    receive = commands.add_parser('receive')
    reply = commands.add_parser('reply')
    for command in (connect, receive, reply):
        command.add_argument('--participant', required=True)
        command.add_argument('--session', default=os.environ.get('CODEX_THREAD_ID'))
    connect.add_argument('--label', required=True)
    reply.add_argument('--job', required=True)
    reply.add_argument('--revision', required=True, type=int)
    reply.add_argument('--text-file', required=True)
    reply.add_argument('--source', action='append', default=[])
    commands.add_parser('state')
    args = parser.parse_args(argv)
    store = Store(args.state_dir)
    try:
        if args.command == 'serve':
            server = ThreadingHTTPServer(('localhost', args.port), handler(store))
            print(f'deus_ex_machina: http://localhost:{server.server_port}', flush=True)
            try:
                server.serve_forever()
            except KeyboardInterrupt:
                pass
            finally:
                server.server_close()
            return 0
        if args.command == 'state':
            result = store.state()
        else:
            if not args.session:
                raise ValueError('Gerçek CLI oturum etiketini --session ile ver.')
            session = store.session_id(args.participant, args.session)
            if args.command == 'connect':
                result = store.connect(args.participant, args.session, args.label)
            elif args.command == 'receive':
                result = store.receive(session)
            else:
                result = store.reply(session, args.job, args.revision,
                                     Path(args.text_file).read_text(encoding='utf-8'), args.source)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (ValueError, OSError, sqlite3.Error) as error:
        print(json.dumps({'error': str(error)}, ensure_ascii=False), file=__import__('sys').stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
