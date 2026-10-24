#!/usr/bin/env python3
"""Ortak Köprü botu: katılımcılara düşen açık kayıtları bulur, üretici API'si ile tek bir yanıt kaydı üretir,
kopru_ekle.py ile ekler ve her çağrının tam bağlamını kayit/ klasörüne yazar. Yalnız standart kütüphane.

Modlar:
  python3 kopru_yanitla.py kopru.html                         # ayarlar.json'daki her katılımcı için bekleyenleri yanıtla
  python3 kopru_yanitla.py kopru.html --kuru                  # API çağırmadan istemleri kur ve kayit/ altına yaz
  python3 kopru_yanitla.py kopru.html --bekleyenler Gemini    # Gemini'ye düşen açık kayıtları JSON listele
  python3 kopru_yanitla.py kopru.html --istem Gemini          # Gemini için istem metnini yaz (CLI katmanları kullanır)
  python3 kopru_yanitla.py kopru.html --ayarlar ayarlar-yerel.json --yalniz Claude   # yalnız bir katılımcıyı çalıştır

Katılımcı ayarları: "saglayici" api adı (anthropic, openai, google) ya da "cli"; cli için "komut" listesi, "istem_nasil"
(dosya | stdin | arg), isteğe bağlı "ortam" (yalnız o komuta verilecek ortam değişkenleri; null değer o değişkeni kaldırır) ve "zaman_asimi" (saniye).
Komut bu makinede yoksa katılımcı sessizce atlanır; atlanan her çalıştırma kayit/atlandi.log'a tek satır düşer.

Bekleyen kaydın tanımı: durumu açık, "kime" alanında katılımcının adı geçen, katılımcının kendi yazmadığı ve
katılımcının daha sonra yazdığı bir kaydın "yanıt" alanının kapsamadığı kayıt. Bir yanıt kaydı, yanıt alanındaki
numaraya kadar olan bütün bekleyenleri kapsar; bu yüzden her çalıştırmada katılımcı başına tek kayıt yeter.

Anahtarlar yalnız ortam değişkeninden okunur ve hiçbir yere yazılmaz.
"""
import argparse, datetime, hashlib, json, os, re, shutil, subprocess, sys, tempfile, urllib.error, urllib.parse, urllib.request
from pathlib import Path

BURASI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURASI)
from kopru_oku import Ayristirici  # noqa: E402


# ---------- sayfa okuma ----------

def kayitlari_oku(yol):
    ay = Ayristirici()
    with open(yol, encoding="utf-8") as fh:
        ay.feed(fh.read())
    return ay.kayitlar


def ad_kok(s):
    """'ChatGPT (Şaman)' → 'ChatGPT'."""
    return (s or "").split("(")[0].strip()


def kime_adlari(s):
    return [ad_kok(x) for x in (s or "").split(",") if x.strip()]


def numara(kid):
    m = re.fullmatch(r"k-(\d{4})", kid or "")
    return int(m.group(1)) if m else -1


def bekleyenler(kayitlar, ad):
    kapsanan_ust = -1
    for k in kayitlar:
        if ad_kok(k["kimden"]) == ad and k.get("yanit"):
            kapsanan_ust = max(kapsanan_ust, numara(k["yanit"]))
    out = []
    for k in kayitlar:
        if k["durum"] != "acik":
            continue
        if ad not in kime_adlari(k["kime"]):
            continue
        if ad_kok(k["kimden"]) == ad:
            continue
        if numara(k["id"]) <= kapsanan_ust:
            continue
        out.append(k)
    return out


def bolum_metni(belge, bolum_id):
    m = re.search(r'<section id="%s"[^>]*>(.*?)</section>' % re.escape(bolum_id), belge, re.S)
    if not m:
        return ""
    t = re.sub(r"<style.*?</style>", "", m.group(1), flags=re.S)
    t = re.sub(r"</(p|li|h[1-6]|tr|div|details|summary)>", "\n", t)
    t = re.sub(r"</t[dh]>", " | ", t)
    t = re.sub(r"<[^>]+>", "", t)
    t = t.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&").replace("&quot;", '"')
    t = "\n".join(l.strip() for l in t.splitlines())
    return re.sub(r"\n{3,}", "\n\n", t).strip()


# ---------- istem ----------

def sablon_oku():
    with open(os.path.join(BURASI, "istem-sablonu.md"), encoding="utf-8") as fh:
        s = fh.read()
    sistem = re.search(r"## Sistem\n(.*?)\n## Kullanıcı\n", s, re.S).group(1).strip()
    kullanici = s.split("## Kullanıcı\n", 1)[1].strip()
    return sistem, kullanici


def istem_kur(yol, ad, bek):
    with open(yol, encoding="utf-8") as fh:
        belge = fh.read()
    kayitlar = kayitlari_oku(yol)
    sistem, kullanici = sablon_oku()
    degerler = {
        "ad": ad,
        "bekleyen_idler": ", ".join(k["id"] for k in bek),
        "hedef_id": bek[-1]["id"],
        "kurallar_metni": bolum_metni(belge, "kurallar"),
        "dosya_metni": bolum_metni(belge, "yonlendirme"),
        "kayitlar_json": json.dumps(kayitlar, ensure_ascii=False, indent=1),
        "bekleyen_json": json.dumps(bek, ensure_ascii=False, indent=1),
    }
    for k, v in degerler.items():
        sistem = sistem.replace("{" + k + "}", v)
        kullanici = kullanici.replace("{" + k + "}", v)
    return sistem, kullanici


def governed_compile(root, page_path, settings_path, participant, pending, route, policy_path):
    """Build an opt-in request from the stable policy/source snapshot; never chooses a fallback implicitly."""
    from kopru_governance.core import GovernanceError, _parse_json, _read_file, compile_context, load_policy, sha256

    root = Path(root).resolve(strict=True)
    page = Path(page_path)
    settings = Path(settings_path)
    if not page.is_absolute():
        page = root / page
    if not settings.is_absolute():
        settings = root / settings
    page = page.resolve(strict=True)
    settings = settings.resolve(strict=True)
    if page != root / "kopru.html":
        raise GovernanceError("governed mode only accepts the repository's canonical kopru.html")
    try:
        settings_rel = settings.relative_to(root).as_posix()
    except ValueError as exc:
        raise GovernanceError("settings file must be inside the repository root") from exc
    policy, _, _ = load_policy(root, policy_path)
    policy_sources = {source["path"]: source for source in policy["sources"]}
    if "kopru.html" not in policy_sources or settings_rel not in policy_sources:
        raise GovernanceError("policy must hash the canonical bridge and selected settings file")
    _, settings_text = _read_file(root, settings_rel)
    settings_data = _parse_json(settings_text, settings_rel)
    if not isinstance(settings_data, dict) or not isinstance(settings_data.get("katilimcilar"), list):
        raise GovernanceError("settings must contain a participant list")
    _, bridge_snapshot = _read_file(root, "kopru.html")
    bridge_parser = Ayristirici()
    bridge_parser.feed(bridge_snapshot)
    current_pending = bekleyenler(bridge_parser.kayitlar, participant)
    if current_pending != pending:
        raise GovernanceError("pending records changed before governed snapshot compilation")
    bridge_hash = sha256(bridge_snapshot.encode("utf-8"))
    participant_config = next(
        (item for item in settings_data.get("katilimcilar", []) if item.get("ad") == participant),
        None,
    )
    if not participant_config:
        raise GovernanceError(f"participant is not configured: {participant}")
    if route == "fallback":
        if not participant_config.get("yedek"):
            raise GovernanceError("no explicit fallback route is configured")
        selected = participant_config["yedek"]
    else:
        selected = participant_config
    provider = selected.get("saglayici")
    model = selected.get("model", "unknown")
    allowed_key_names = {
        "anthropic": "ANTHROPIC_API_KEY",
        "openai": "OPENAI_API_KEY",
        "google": "GEMINI_API_KEY",
    }
    if provider in allowed_key_names and selected.get("anahtar_degiskeni") != allowed_key_names[provider]:
        raise GovernanceError("provider credential variable is not in the governed allowlist")
    limits = policy["limits"]
    request = {
        "participant": participant,
        "route_requested": route,
        "provider": provider,
        "model": model,
        "reasoning_requested": selected.get("dusunme"),
        "credential_variable_name": selected.get("anahtar_degiskeni"),
        "max_output_tokens": limits["max_output_tokens"],
        "timeout_seconds": limits["timeout_seconds"],
        "tools": policy["allowed_tools"],
    }
    task = (
        "Prepare one draft response to the explicitly listed pending bridge records. "
        "Return the bridge's JSON fields only. Do not modify files or perform external actions."
    )
    compiled = compile_context(
        root, task, request, policy_path,
        task_data={"participant": participant, "pending_records": pending},
    )
    if compiled["source_hashes"].get(settings_rel) != sha256(settings_text.encode("utf-8")):
        raise GovernanceError("settings changed between route selection and context compilation")
    if compiled["source_hashes"].get("kopru.html") != bridge_hash:
        raise GovernanceError("bridge changed between pending-record selection and context compilation")
    return compiled, selected


def _write_plan(compiled, output):
    from kopru_governance.core import GovernanceError
    from kopru_governance.runs import write_private_artifact

    root = Path(BURASI).resolve()
    runs_root = root / "runs"
    if runs_root.is_symlink():
        raise GovernanceError("runs/ may not be a symlink")
    output = Path(output)
    if not output.is_absolute():
        output = root / output
    output = Path(os.path.abspath(output))
    try:
        relative = output.relative_to(runs_root)
    except ValueError as exc:
        raise GovernanceError("governed plan must be stored under ignored runs/") from exc
    if not relative.parts or any(part in ("", ".", "..") for part in relative.parts):
        raise GovernanceError("unsafe governed plan path")
    current = runs_root
    for part in relative.parts[:-1]:
        current = current / part
        if current.is_symlink():
            raise GovernanceError("plan directories may not be symlinks")
    if output.is_symlink():
        raise GovernanceError("plan file may not be a symlink")
    data = compiled["bundle_bytes"]
    if output.exists():
        if output.read_bytes() != data:
            raise GovernanceError("existing plan path contains different data; choose another path")
        try:
            output.chmod(0o600)
        except OSError:
            pass
    else:
        write_private_artifact(root, output, data)
    return output


def governed_execute(root, compiled, selected, approval_path, runs_dir):
    from kopru_governance.execute import execute_once

    key_holder = {"value": ""}
    variable = selected.get("anahtar_degiskeni")

    def preflight():
        if selected.get("saglayici") not in ("anthropic", "openai", "google"):
            raise RuntimeError("CLI adapters are not enabled in this MVP")
        if not variable or not os.environ.get(variable):
            raise RuntimeError("provider credentials unavailable")
        key_holder["value"] = os.environ[variable]

    def call(provider, model, messages, max_output_tokens, timeout_seconds, reasoning, on_request):
        return governed_api_call(
            provider, model, key_holder["value"], messages,
            max_output_tokens, timeout_seconds, reasoning, on_request,
        )

    return execute_once(root, compiled, approval_path, runs_dir, call, preflight)


# ---------- üretici çağrıları ----------

class _NoRedirectHandler(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def http_json(url, veri, basliklar, zaman_asimi=180, safe_errors=False, on_request=None):
    body = json.dumps(veri, ensure_ascii=not bool(on_request)).encode("utf-8")
    if on_request and len(body) > 16 * 1024 * 1024:
        raise RuntimeError("governed provider request exceeds the 16 MiB limit")
    if on_request:
        parsed = urllib.parse.urlsplit(url)
        on_request({
            "request_body_sha256": hashlib.sha256(body).hexdigest(),
            "target": parsed.netloc + parsed.path,
        })
    istek = urllib.request.Request(url, data=body, headers={"Content-Type": "application/json", **basliklar}, method="POST")
    try:
        if on_request:
            response = urllib.request.build_opener(_NoRedirectHandler()).open(istek, timeout=zaman_asimi)
        else:
            response = urllib.request.urlopen(istek, timeout=zaman_asimi)
        with response as y:
            response = y.read(16 * 1024 * 1024 + 1) if on_request else y.read()
            if on_request and len(response) > 16 * 1024 * 1024:
                raise RuntimeError("governed provider response exceeds the 16 MiB limit")
            return json.loads(response.decode("utf-8"))
    except urllib.error.HTTPError as e:
        if safe_errors:
            raise ProviderHTTPError(e.code) from None
        govde = e.read().decode("utf-8", errors="replace")[:2000]
        raise RuntimeError(f"HTTP {e.code}: {govde}") from None


class ProviderHTTPError(RuntimeError):
    """Safe provider status only; deliberately excludes the response body."""

    def __init__(self, status_code):
        self.status_code = status_code
        super().__init__(f"HTTP {status_code}: provider response body redacted")


class KomutYok(Exception):
    """CLI komutu bu makinede yok (kurulmamış ya da yol yanlış). Sessiz atlanır, kayıt dosyası yazılmaz."""


def komut_var_mi(komut):
    """Komutun ilk ögesi tam yolsa dosya var mı, değilse PATH'te bulunuyor mu bakar."""
    exe = komut[0]
    if os.sep in exe or (os.altsep and os.altsep in exe) or (len(exe) > 1 and exe[1] == ":"):
        return os.path.isfile(exe)
    return shutil.which(exe) is not None


def cli_cagir(komut, sistem, kullanici, istem_nasil="dosya", ad="bot", zaman_asimi=1800, ortam=None):
    """Abonelikle çalışan bir CLI'ı (claude -p, codex exec, gemini -p) etkileşimsiz çalıştırır; standart çıktı yanıttır.
    istem_nasil: "dosya" → istem istem-<ad>.txt dosyasına yazılır, komuttaki {dosya} yer tutucusu adıyla değiştirilir
                 (Windows komut satırı sınırını aşmaz; CLI dosyayı kendi okur);
                 "stdin" → istem standart girdiden verilir (ssh üzerinden uzak makinedeki CLI için de);
                 "arg"   → istem son argüman olur (yalnız kısa istemler, Linux/macOS).
    ortam: yalnız bu komut için eklenecek ortam değişkenleri (ör. CLI'ın kendi HOME'u); süreç ortamının üstüne yazılır.
    Çıktı her zaman UTF-8 okunur (Windows'ta konsol kod sayfasına bağlı kalmaz)."""
    istem = sistem + "\n\n---\n\n" + kullanici
    komut = list(komut)
    if not komut_var_mi(komut):
        raise KomutYok(komut[0])
    cevre = dict(os.environ)
    for k, v in (ortam or {}).items():   # null → değişken kaldırılır (ör. OPENAI_API_KEY: Codex API yoluna sapmasın)
        if v is None:
            cevre.pop(k, None)
        else:
            cevre[k] = str(v)
    secenek = dict(capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=zaman_asimi, cwd=BURASI, env=cevre)
    if istem_nasil == "dosya":
        dosya = f"istem-{re.sub(r'[^A-Za-z0-9]+', '-', ad).strip('-')}.txt"
        open(os.path.join(BURASI, dosya), "w", encoding="utf-8").write(istem)
        komut = [c.replace("{dosya}", dosya) for c in komut]
        sonuc = subprocess.run(komut, **secenek)
    elif istem_nasil == "stdin":
        sonuc = subprocess.run(komut, input=istem, **secenek)
    else:
        sonuc = subprocess.run(komut + [istem], **secenek)
    if sonuc.returncode != 0:
        raise RuntimeError(f"CLI çıkış kodu {sonuc.returncode}: {(sonuc.stderr or sonuc.stdout)[-1500:]}")
    return sonuc.stdout, {"cli": " ".join(komut), "stderr_son": (sonuc.stderr or "")[-300:]}


def cagir(saglayici, model, anahtar, sistem, kullanici, en_cok_token, caba=None):
    """Üretici API'sini çağırır. Derin düşünme ayarı (caba) 400 verirse bir alt düzeyle, sonra ayarsız yeniden dener."""
    denemeler = [caba, "high", None] if caba and caba != "high" else ([caba, None] if caba else [None])
    son_hata = None
    for c in denemeler:
        try:
            if saglayici == "anthropic":
                govde = {"model": model, "max_tokens": en_cok_token, "system": sistem, "messages": [{"role": "user", "content": kullanici}]}
                y = http_json("https://api.anthropic.com/v1/messages", govde, {"x-api-key": anahtar, "anthropic-version": "2023-06-01"})
                return "".join(p.get("text", "") for p in y.get("content", []) if p.get("type") == "text"), y.get("usage")
            if saglayici == "openai":
                govde = {"model": model, "instructions": sistem, "input": kullanici, "max_output_tokens": en_cok_token}
                if c:
                    govde["reasoning"] = {"effort": c}
                y = http_json("https://api.openai.com/v1/responses", govde, {"Authorization": f"Bearer {anahtar}"})
                metin = []
                for oge in y.get("output", []):
                    if oge.get("type") == "message":
                        for par in oge.get("content", []):
                            if par.get("type") == "output_text":
                                metin.append(par.get("text", ""))
                return "".join(metin), y.get("usage")
            if saglayici == "google":
                uretim = {"maxOutputTokens": en_cok_token}
                if c:
                    uretim["thinkingConfig"] = {"thinkingLevel": c}
                govde = {"system_instruction": {"parts": [{"text": sistem}]}, "contents": [{"role": "user", "parts": [{"text": kullanici}]}], "generationConfig": uretim}
                y = http_json(f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent", govde, {"x-goog-api-key": anahtar})
                parcalar = y["candidates"][0]["content"]["parts"]
                return "".join(p.get("text", "") for p in parcalar if not p.get("thought")), y.get("usageMetadata")
            raise ValueError(f"bilinmeyen sağlayıcı: {saglayici}")
        except RuntimeError as e:
            son_hata = e
            if c is None or not str(e).startswith("HTTP 400"):
                raise
            print(f"  {saglayici}: düşünme ayarı '{c}' kabul edilmedi, bir alt düzey deneniyor")
    raise son_hata


def governed_api_call(saglayici, model, anahtar, messages, en_cok_token, zaman_asimi, caba=None, on_request=None):
    """One API request only; this path never retries or downgrades a requested setting."""
    sistem = messages[0]["content"]
    kullanici = messages[1]["content"]
    if saglayici == "anthropic":
        govde = {
            "model": model, "max_tokens": en_cok_token, "system": sistem,
            "messages": [{"role": "user", "content": kullanici}],
        }
        y = http_json(
            "https://api.anthropic.com/v1/messages", govde,
            {"x-api-key": anahtar, "anthropic-version": "2023-06-01"},
            zaman_asimi, safe_errors=True, on_request=on_request,
        )
        text = "".join(p.get("text", "") for p in y.get("content", []) if p.get("type") == "text")
        usage = y.get("usage")
    elif saglayici == "openai":
        govde = {
            "model": model, "instructions": sistem, "input": kullanici,
            "max_output_tokens": en_cok_token,
        }
        if caba:
            govde["reasoning"] = {"effort": caba}
        y = http_json(
            "https://api.openai.com/v1/responses", govde,
            {"Authorization": "Bearer " + anahtar}, zaman_asimi, safe_errors=True,
            on_request=on_request,
        )
        text = "".join(
            part.get("text", "")
            for item in y.get("output", []) if item.get("type") == "message"
            for part in item.get("content", []) if part.get("type") == "output_text"
        )
        usage = y.get("usage")
    elif saglayici == "google":
        generation = {"maxOutputTokens": en_cok_token}
        if caba:
            generation["thinkingConfig"] = {"thinkingLevel": caba}
        govde = {
            "system_instruction": {"parts": [{"text": sistem}]},
            "contents": [{"role": "user", "parts": [{"text": kullanici}]}],
            "generationConfig": generation,
        }
        y = http_json(
            f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent",
            govde, {"x-goog-api-key": anahtar}, zaman_asimi, safe_errors=True,
            on_request=on_request,
        )
        parts = y["candidates"][0]["content"]["parts"]
        text = "".join(part.get("text", "") for part in parts if not part.get("thought"))
        usage = y.get("usageMetadata")
    else:
        raise ValueError("governed execution supports only the configured API adapters")
    return text, {
        "provider_observed": "unknown",
        "model_observed": y.get("model", "unknown"),
        "reasoning_requested": caba,
        "reasoning_applied": "unknown",
        "usage_metadata": usage,
    }


# ---------- yanıt işleme ----------

def json_ayikla(metin):
    i, j = metin.find("{"), metin.rfind("}")
    if i < 0 or j < 0:
        raise ValueError("yanıtta JSON nesnesi yok")
    return json.loads(metin[i:j + 1])


def kayit_yaz(ad, model, saglayici, sistem, kullanici, ham, sonuc):
    os.makedirs(os.path.join(BURASI, "kayit"), exist_ok=True)
    zaman = datetime.datetime.now(datetime.UTC).strftime("%Y%m%d-%H%M%SZ")
    guvenli_ad = re.sub(r"[^A-Za-z0-9]+", "-", ad).strip("-")
    yol = os.path.join(BURASI, "kayit", f"{zaman}-{guvenli_ad}.md")
    with open(yol, "w", encoding="utf-8") as fh:
        fh.write(f"# {ad} · {saglayici} · {model} · {zaman}\n\n## Sonuç\n\n{sonuc}\n\n## Sistem istemi\n\n```\n{sistem}\n```\n\n## Kullanıcı iletisi\n\n```\n{kullanici}\n```\n\n## Ham yanıt\n\n```\n{ham}\n```\n")
    return yol


def atlandi_yaz(ad, hatalar):
    """Yol bulunamayınca her çalıştırmada koca bir kayıt dosyası yerine kayit/atlandi.log'a tek satır düşer."""
    os.makedirs(os.path.join(BURASI, "kayit"), exist_ok=True)
    zaman = datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%d %H:%M:%SZ")
    with open(os.path.join(BURASI, "kayit", "atlandi.log"), "a", encoding="utf-8") as fh:
        fh.write(f"{zaman} {ad}: {' | '.join(hatalar)}\n")


def ekle(yol, veri):
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8", dir=BURASI) as fh:
        json.dump(veri, fh, ensure_ascii=False)
        gecici = fh.name
    try:
        sonuc = subprocess.run([sys.executable, "-I", "-X", "utf8", os.path.join(BURASI, "kopru_ekle.py"), yol, "--json", gecici],
                               capture_output=True, text=True, encoding="utf-8", errors="replace")
    finally:
        os.unlink(gecici)
    if sonuc.returncode != 0:
        raise RuntimeError((sonuc.stdout + sonuc.stderr).strip())
    return sonuc.stdout.strip().splitlines()[-1]


def main():
    for akis in (sys.stdout, sys.stderr):  # Windows konsolunda Türkçe karakterler için
        if hasattr(akis, "reconfigure"):
            akis.reconfigure(encoding="utf-8", errors="replace")
    p = argparse.ArgumentParser()
    p.add_argument("dosya")
    p.add_argument("--ayarlar", default=os.path.join(BURASI, "ayarlar.json"))
    p.add_argument("--kuru", action="store_true", help="API çağırma; istemleri kur ve kayit/ altına yaz")
    p.add_argument("--bekleyenler", metavar="AD", help="yalnız listele")
    p.add_argument("--istem", metavar="AD", help="istem metnini yaz ve çık")
    p.add_argument("--yalniz", metavar="AD", help="ayarlardaki katılımcılardan yalnız bunu çalıştır")
    governed = p.add_mutually_exclusive_group()
    governed.add_argument("--governed", action="store_true", help="tek, onaylı governed provider çağrısı")
    governed.add_argument("--plan-governed", action="store_true", help="tam mesajları inceleme için derle; çağrı yapma")
    p.add_argument("--governance-policy", default="policy/policy.json")
    p.add_argument("--approval", help="yerel, kapsamı hash'lerle bağlı onay JSON'u")
    p.add_argument("--plan-output", help="derlenmiş plan yolu (runs/ altında)")
    p.add_argument("--governed-route", choices=("primary", "fallback"), default="primary",
                   help="fallback ancak bu seçenekle açıkça seçilir")
    p.add_argument("--runs-dir", default="runs", help="yalnız repo içindeki runs/ altında olabilir")
    a = p.parse_args()

    kayitlar = kayitlari_oku(a.dosya)
    if a.bekleyenler:
        print(json.dumps(bekleyenler(kayitlar, a.bekleyenler), ensure_ascii=False, indent=1))
        return
    if a.istem:
        bek = bekleyenler(kayitlar, a.istem)
        if not bek:
            print("", end="")
            return
        sistem, kullanici = istem_kur(a.dosya, a.istem, bek)
        print(sistem + "\n\n---\n\n" + kullanici)
        return

    with open(a.ayarlar, encoding="utf-8") as fh:
        ayar = json.load(fh)
    en_cok = int(ayar.get("en_cok_cikti_token", 1500))
    if a.governed or a.plan_governed:
        from kopru_governance.core import GovernanceError, pretty_json

        if a.governed and a.kuru:
            raise SystemExit("HATA: --governed ile legacy --kuru birlikte kullanılamaz.")
        if not a.yalniz:
            raise SystemExit("HATA: governed modda tek katılımcı için --yalniz AD gerekli.")
        if a.governed and not a.approval:
            raise SystemExit("HATA: --governed için --approval gerekli; önce --plan-governed ile mesajları incele.")
        participant = next((item for item in ayar["katilimcilar"] if item["ad"] == a.yalniz), None)
        if participant is None:
            raise SystemExit(f"HATA: ayarlarda katılımcı yok: {a.yalniz}")
        pending = bekleyenler(kayitlar, a.yalniz)
        if not pending:
            print(f"{a.yalniz}: bekleyen yok; çağrı yapılmadı")
            return
        compiled, selected = governed_compile(
            BURASI, a.dosya, a.ayarlar, a.yalniz, pending,
            a.governed_route, a.governance_policy,
        )
        root = Path(BURASI).resolve()
        if a.plan_governed:
            plan_path = _write_plan(
                compiled,
                a.plan_output or f"runs/plans/{compiled['bundle']['manifest']['context_hash']}.json",
            )
            approval_path = plan_path.with_suffix(".approval.json")
            approval = {
                "granted": False,
                "approved_by": "",
                "operation": "provider_call",
                "scope": {
                    "policy_sha256": compiled["policy_hash"],
                    "context_hash": compiled["bundle"]["manifest"]["context_hash"],
                    "source_hashes": compiled["source_hashes"],
                },
                "expires_at": "",
            }
            if approval_path.is_symlink():
                raise GovernanceError("approval template may not be a symlink")
            if not approval_path.exists():
                from kopru_governance.runs import write_private_artifact
                write_private_artifact(root, approval_path, pretty_json(approval))
            else:
                try:
                    approval_path.chmod(0o600)
                except OSError:
                    pass
            print(json.dumps({
                "plan": str(plan_path.relative_to(root)),
                "approval_template": str(approval_path.relative_to(root)),
                "context_hash": compiled["bundle"]["manifest"]["context_hash"],
                "visibility": compiled["bundle"]["manifest"]["visibility"],
                "provider_requested": selected.get("saglayici"),
                "model_requested": selected.get("model", "unknown"),
            }, ensure_ascii=False, indent=2))
            for message in compiled["bundle"]["messages"]:
                print(f"\n--- EXACT MESSAGE ROLE: {message['role']} ---\n{message['content']}")
            return

        runs_dir = Path(a.runs_dir)
        if not runs_dir.is_absolute():
            runs_dir = root / runs_dir
        if (root / "runs").is_symlink() or runs_dir.resolve() != (root / "runs").resolve():
            raise GovernanceError("run ledger path must be exactly the repository's ignored runs/ directory")
        approval_path = Path(a.approval)
        if approval_path.is_absolute():
            raise GovernanceError("approval path must be repository-relative")
        result = governed_execute(root, compiled, selected, a.approval, runs_dir)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return

    eklenenler = []
    for kat in ayar["katilimcilar"]:
        ad = kat["ad"]
        if a.yalniz and ad != a.yalniz:
            continue
        bek = bekleyenler(kayitlar, ad)
        if not bek:
            print(f"{ad}: bekleyen yok")
            continue
        sistem, kullanici = istem_kur(a.dosya, ad, bek)
        if a.kuru:
            yol = kayit_yaz(ad, kat.get("model", "-"), kat["saglayici"], sistem, kullanici, "(kuru çalıştırma, çağrı yapılmadı)", "kuru")
            print(f"{ad}: {len(bek)} bekleyen; istem {yol} dosyasına yazıldı")
            continue
        # Yollar: asıl yol, sonra varsa "yedek". Her yol için gereken ortam değişkeni (anahtar ya da abonelik belirteci) yoksa o yol atlanır.
        yollar = [kat] + ([kat["yedek"]] if kat.get("yedek") else [])
        ham, kullanim, kullanilan, hatalar = "", None, None, []
        for yol_ayar in yollar:
            degisken = yol_ayar.get("anahtar_degiskeni")
            anahtar = (os.environ.get(degisken, "") or "").strip() if degisken else ""   # boş ya da boşluk değer = yok
            if degisken and not anahtar:
                hatalar.append(f"{yol_ayar['saglayici']}: {degisken} yok")
                continue
            try:
                if yol_ayar["saglayici"] == "cli":
                    ham, kullanim = cli_cagir(yol_ayar["komut"], sistem, kullanici, yol_ayar.get("istem_nasil", "dosya"), ad,
                                              int(yol_ayar.get("zaman_asimi", 1800)), yol_ayar.get("ortam"))
                else:
                    ham, kullanim = cagir(yol_ayar["saglayici"], yol_ayar["model"], anahtar, sistem, kullanici, en_cok, yol_ayar.get("dusunme"))
                kullanilan = yol_ayar
                break
            except KomutYok as e:
                hatalar.append(f"{yol_ayar['saglayici']}: komut yok: {e}")
            except Exception as e:  # noqa: BLE001
                hatalar.append(f"{yol_ayar['saglayici']}: {str(e)[:300]}")
        if kullanilan is None:
            atlandi_yaz(ad, hatalar)
            print(f"{ad}: atlandı ({' | '.join(hatalar)[:200]}) → kayit/atlandi.log")
            continue
        try:
            veri = json_ayikla(ham)
            veri["kimden"] = kullanilan.get("imza") or kat.get("imza") or f"{ad} (API)"
            veri.setdefault("kime", "Sen")
            veri["yanit"] = bek[-1]["id"]
            veri["durum"] = "acik"
            veri.setdefault("dayanak", "")
            kid = ekle(a.dosya, veri)
            sonuc = f"eklendi: {kid}; yol: {kullanilan['saglayici']} {kullanilan.get('model', '')}; bekleyenler: {', '.join(k['id'] for k in bek)}; kullanım: {json.dumps(kullanim, ensure_ascii=False)}"
            eklenenler.append(kid)
        except Exception as e:  # noqa: BLE001
            sonuc = f"HATA: {e}"
        yol = kayit_yaz(ad, kullanilan.get("model", "-"), kullanilan["saglayici"], sistem, kullanici, ham, sonuc)
        print(f"{ad}: {sonuc.splitlines()[0][:200]} → {os.path.relpath(yol, BURASI)}")
    print("eklenen:", ", ".join(eklenenler) if eklenenler else "yok")


if __name__ == "__main__":
    main()
