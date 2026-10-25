"""Block maintenance races and reintroduction of specifically withdrawn Git ancestry."""
import json
from pathlib import Path
import subprocess
import sys

policy=json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
data=sys.stdin.buffer.read()
if Path(policy['maintenance_flag']).exists():
    print('HalukAI: gizlilik bakimi suruyor; calisma korunuyor, gonderim bekletildi.',file=sys.stderr)
    raise SystemExit(1)
cwd=Path.cwd().resolve()
base=['git','-c','safe.directory='+cwd.as_posix()]
for row in data.decode().splitlines():
    fields=row.split()
    if len(fields)!=4:raise SystemExit('Unexpected pre-push input')
    head=fields[1]
    if set(head)=={'0'}:continue
    for old in policy.get('withdrawn_ancestors',[]):
        result=subprocess.run(base+['merge-base','--is-ancestor',old,head],capture_output=True)
        if result.returncode==0:
            print('HalukAI: geri cekilen ozel gecmis yeniden yayimlanamaz; temiz dala rebase gerekli.',file=sys.stderr)
            raise SystemExit(1)
    blocked=set(policy.get('withdrawn_blob_ids',[]))
    if blocked:
        objects=subprocess.run(base+['rev-list','--objects',head],capture_output=True,check=True).stdout
        if blocked.intersection(line.split()[0].decode() for line in objects.splitlines()):
            print('HalukAI: ozel kaynaktan geri cekilen dosya govdesi tekrar yayimlanamaz.',file=sys.stderr)
            raise SystemExit(1)
if len(sys.argv)>2 and sys.argv[2] and Path(sys.argv[2]).is_file():
    raise SystemExit(subprocess.run(['sh',sys.argv[2],*sys.argv[3:]],input=data).returncode)
