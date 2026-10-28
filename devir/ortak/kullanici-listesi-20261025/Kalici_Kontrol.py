"""Observe Y: persistence on normal starts; never close a session or restart Windows."""
import ctypes
import datetime as dt
import hashlib
import json
from pathlib import Path
import subprocess

root=Path('Y:/HalukAI/Ortak_Kopru')
directory=root/'Kalicilik_Kontrolu';directory.mkdir(exist_ok=True)
state_path=directory/'durum.json'
previous=json.loads(state_path.read_text(encoding='utf-8')) if state_path.exists() else None
sentinel=directory/'Y_KALICILIK_ISARETI.txt'
content=b'HALUKAI_Y_KALICILIK_GOZLEMI_20261025\n'
if previous is None:
    with sentinel.open('xb') as stream:stream.write(content)
stamp=subprocess.run(['Y:/HalukAI/02_Govde/Canli/CLI_Katmanlari/Runtime/PowerShell-7.6.8-win-x64/pwsh.exe',
    '-NoProfile','-Command',"$b=Get-CimInstance Win32_OperatingSystem -ErrorAction Stop; $b.LastBootUpTime.ToUniversalTime().ToString('o')"],
    capture_output=True,timeout=15)
boot=stamp.stdout.decode('utf-8-sig',errors='replace').strip() if stamp.returncode==0 else None
names=['Geçmiş.txt','Durum Bildirimi.txt','İlerisi.txt','deus_ex_machina.txt','Steering Arşiv.txt',
    'GitHub Ortak-Kopru.txt','Klavye Çizimleri.txt','Kullanıcıdan İstenenler.txt']
files={name:(root/'Ortak_Notlar/Kullanici_Anlatisi'/name).is_file() for name in names}
observed_new_boot=bool(previous and boot and previous.get('windows_boot_utc') and previous['windows_boot_utc']!=boot)
uptime=ctypes.windll.kernel32.GetTickCount64
uptime.restype=ctypes.c_ulonglong
result={'at_utc':dt.datetime.now(dt.timezone.utc).isoformat(),'windows_boot_utc':boot,
    'windows_uptime_ms':uptime(),
    'sentinel_matches':sentinel.is_file() and sentinel.read_bytes()==content,'user_documents_present':files,
    'google_session_state_on_y':Path('Y:/HalukAI/02_Govde/Canli/CLI_Katmanlari/02_Copilot_Sahit/Sahit_Ultra_Durum.json').is_file(),
    'observed_different_windows_boot':observed_new_boot,
    'reboot_persistence_observed':bool((observed_new_boot or (previous or {}).get('reboot_persistence_observed'))
        and all(files.values()) and sentinel.is_file() and sentinel.read_bytes()==content),
    'windows_restarted_by_check':False,'model_invoked':False}
with (directory/'gozlemler.jsonl').open('ab') as stream:stream.write((json.dumps(result,ensure_ascii=False)+'\n').encode())
temporary=directory/'~durum-yeni.json'
temporary.write_bytes((json.dumps(result,ensure_ascii=False,indent=2)+'\n').encode())
temporary.replace(state_path)
print(json.dumps({'persistence_baseline_recorded':True,'documents_present':all(files.values()),
    'different_boot_observed':observed_new_boot,'reboot_persistence_observed':result['reboot_persistence_observed'],
    'live_sessions_closed':False,'model_invoked':False}))
