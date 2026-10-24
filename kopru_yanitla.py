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
import argparse, contextvars, datetime, hashlib, json, os, re, shutil, subprocess, sys, tempfile, urllib.error, urllib.request

BURASI = os.path.dirname(os.path.abspath(__file__))
API_TIMEOUT = contextvars.ContextVar("kopru_api_timeout", default=180)
API_RESPONSE_LIMIT = contextvars.ContextVar("kopru_api_response_limit", default=None)
sys.path.insert(0, BURASI)
from kopru_oku import Ayristirici  # noqa: E402


# ---------- sayfa okuma ----------

def kayitlari_oku(yol):
    ay = Ayristirici()
    ay.feed(open(yol, encoding="utf-8").read())
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
    s = open(os.path.join(BURASI, "istem-sablonu.md"), encoding="utf-8").read()
    sistem = re.search(r"## Sistem\n(.*?)\n## Kullanıcı\n", s, re.S).group(1).strip()
    kullanici = s.split("## Kullanıcı\n", 1)[1].strip()
    return sistem, kullanici


def istem_kur(yol, ad, bek):
    belge = open(yol, encoding="utf-8").read()
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


# ---------- üretici çağrıları ----------

def http_json(url, veri, basliklar, zaman_asimi=None):
    istek = urllib.request.Request(url, data=json.dumps(veri).encode("utf-8"), headers={"Content-Type": "application/json", **basliklar}, method="POST")
    try:
        with urllib.request.urlopen(istek, timeout=zaman_asimi if zaman_asimi is not None else API_TIMEOUT.get()) as y:
            limit = API_RESPONSE_LIMIT.get()
            if limit is None:
                response = y.read()
            else:
                response = bytearray()
                while len(response) <= limit:
                    chunk = y.read(min(65536, limit + 1 - len(response)))
                    if not chunk:
                        break
                    response.extend(chunk)
                if len(response) > limit:
                    raise RuntimeError("Provider response exceeded the policy byte limit")
            return json.loads(bytes(response).decode("utf-8"))
    except urllib.error.HTTPError as e:
        govde = e.read().decode("utf-8", errors="replace")[:2000]
        raise RuntimeError(f"HTTP {e.code}: {govde}") from None


def api_istek_hash(veri):
    """Hash the exact UTF-8 JSON body serialization used by http_json."""
    return hashlib.sha256(json.dumps(veri).encode("utf-8")).hexdigest()


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


def cagir(saglayici, model, anahtar, sistem, kullanici, en_cok_token, caba=None, allow_fallback=True,
          return_metadata=False):
    """Üretici API'sini çağırır. Derin düşünme ayarı (caba) 400 verirse bir alt düzeyle, sonra ayarsız yeniden dener."""
    if allow_fallback:
        denemeler = [caba, "high", None] if caba and caba != "high" else ([caba, None] if caba else [None])
    else:
        denemeler = [caba] if caba else [None]
    son_hata = None
    for c in denemeler:
        try:
            if saglayici == "anthropic":
                govde = {"model": model, "max_tokens": en_cok_token, "system": sistem, "messages": [{"role": "user", "content": kullanici}]}
                y = http_json("https://api.anthropic.com/v1/messages", govde, {"x-api-key": anahtar, "anthropic-version": "2023-06-01"})
                sonuc = ("".join(p.get("text", "") for p in y.get("content", []) if p.get("type") == "text"), y.get("usage"))
                return (*sonuc, {"request_body_sha256": api_istek_hash(govde), "observed_model": y.get("model"), "reasoning_sent": None}) if return_metadata else sonuc
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
                sonuc = ("".join(metin), y.get("usage"))
                return (*sonuc, {"request_body_sha256": api_istek_hash(govde), "observed_model": y.get("model"), "reasoning_sent": c}) if return_metadata else sonuc
            if saglayici == "google":
                uretim = {"maxOutputTokens": en_cok_token}
                if c:
                    uretim["thinkingConfig"] = {"thinkingLevel": c}
                govde = {"system_instruction": {"parts": [{"text": sistem}]}, "contents": [{"role": "user", "parts": [{"text": kullanici}]}], "generationConfig": uretim}
                y = http_json(f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent", govde, {"x-goog-api-key": anahtar})
                parcalar = y["candidates"][0]["content"]["parts"]
                sonuc = ("".join(p.get("text", "") for p in parcalar if not p.get("thought")), y.get("usageMetadata"))
                return (*sonuc, {"request_body_sha256": api_istek_hash(govde), "observed_model": y.get("modelVersion"), "reasoning_sent": c}) if return_metadata else sonuc
            raise ValueError(f"bilinmeyen sağlayıcı: {saglayici}")
        except RuntimeError as e:
            son_hata = e
            if not allow_fallback or c is None or not str(e).startswith("HTTP 400"):
                raise
            print(f"  {saglayici}: düşünme ayarı '{c}' kabul edilmedi, bir alt düzey deneniyor")
    raise son_hata


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


def denetlenebilir_cagir(kat, artifact_path, approval_path, policy_path, bridge_path=None, config_path=None):
    """Run one explicitly approved API call; local CLI adapters are intentionally unsupported."""
    from ortak_kopru.context import ContextError, consume_approval, load_json, validate_policy, verify_approval, verify_compiled
    from ortak_kopru.runs import RunStore, contains_secret

    compiled = load_json(artifact_path)
    policy = validate_policy(load_json(policy_path))
    digest = verify_compiled(compiled)
    manifest = {source["path"]: source["role"] for source in compiled.get("sources", [])}
    if manifest.get("kopru.html") != "untrusted_evidence":
        raise ContextError("Audited context must include the canonical bridge as untrusted evidence")
    if manifest.get("ayarlar.json") != "configuration":
        raise ContextError("Audited context must include the canonical provider configuration")
    if bridge_path is None or os.path.abspath(bridge_path) != os.path.join(BURASI, "kopru.html"):
        raise ContextError("Audited context is bound to the canonical kopru.html path")
    if config_path is None or os.path.abspath(config_path) != os.path.join(BURASI, "ayarlar.json"):
        raise ContextError("Audited context is bound to the canonical ayarlar.json configuration")
    messages = compiled.get("messages")
    if not isinstance(messages, list) or len(messages) != 2 or [m.get("role") for m in messages] != ["system", "user"]:
        raise ContextError("Audited context must contain exactly one system and one user message")
    if contains_secret(messages):
        raise ContextError("Outgoing context matched a secret-like pattern; provider call was blocked")
    if kat["saglayici"] == "cli":
        raise ContextError("Audited execution currently supports only direct API adapters; CLI hidden layers are not fully captured")
    if compiled["provider"]["requested"] != kat["saglayici"] or compiled["provider"]["model_requested"] != kat.get("model"):
        raise ContextError("Requested provider/model differs from the reviewed compiled context")
    reasoning = kat.get("dusunme") or "none"
    if compiled["provider"]["reasoning_requested"] != reasoning:
        raise ContextError("Requested reasoning differs from the reviewed compiled context")
    if kat["saglayici"] == "anthropic" and reasoning != "none":
        raise ContextError("This Anthropic adapter does not send a reasoning setting")
    if reasoning not in policy["provider"]["allowed_reasoning"]:
        raise ContextError("Requested reasoning is not allowed by policy")

    if not approval_path:
        print(f"Onay yok; sağlayıcı çağrısı yapılmadı. Bağlam SHA-256: {digest}")
        print("İncelenen gerçek mesajlar:")
        print(json.dumps(messages, ensure_ascii=False, indent=2))
        print(f"Onay için: python -m ortak_kopru.cli approve --artifact {artifact_path} --policy {policy_path} --expires <UTC-ISO> --confirm-reviewed")
        return None
    verify_approval(compiled, policy, policy_path, approval_path, BURASI)

    degisken = kat.get("anahtar_degiskeni")
    anahtar = (os.environ.get(degisken, "") or "").strip() if degisken else ""
    if degisken and not anahtar:
        raise ContextError(f"Required environment key is not set: {degisken}")
    timeout = int(policy["limits"]["timeout_seconds"])
    token_limit = int(policy["limits"].get("max_output_tokens", 0))
    if token_limit < 1:
        raise ContextError("Policy must set a positive max_output_tokens")
    if int(policy["limits"]["max_rounds"]) != 1:
        raise ContextError("This audited adapter supports exactly one request round")

    run = RunStore(os.path.join(BURASI, "runs")).start(
        compiled,
        {
            "provider_requested": kat["saglayici"],
            "model_requested": kat["model"],
            "reasoning_requested": reasoning,
            "max_rounds": 1,
        },
    )
    # Both records must exist before any network call; failure here is fail-closed.
    try:
        consume_approval(approval_path)
    except ContextError:
        run.append("skipped", {"reason": "approval_unavailable"})
        raise
    run.append(
        "attempted",
        {"provider_requested": kat["saglayici"], "model_requested": kat["model"]},
        raw={"messages": messages, "context_sha256": digest},
    )
    api_token = API_TIMEOUT.set(timeout)
    response_token = API_RESPONSE_LIMIT.set(int(policy["limits"]["max_output_bytes"]) + 65536)
    try:
        ham, kullanim, metadata = cagir(
            kat["saglayici"],
            kat["model"],
            anahtar,
            messages[0]["content"],
            messages[1]["content"],
            token_limit,
            None if reasoning == "none" else reasoning,
            allow_fallback=False,
            return_metadata=True,
        )
    except Exception as exc:  # provider error bodies remain in the private local raw event only
        try:
            run.append("failed", {"error_type": type(exc).__name__}, raw={"error": str(exc)})
        except Exception as record_error:
            try:
                run.append("recovery_required", {"recording_error_type": type(record_error).__name__})
            except Exception:
                pass
            raise ContextError(f"Provider call failed; recovery required because run recording failed ({type(record_error).__name__})") from None
        raise ContextError(f"Provider call failed ({type(exc).__name__}); details were kept local") from None
    finally:
        API_RESPONSE_LIMIT.reset(response_token)
        API_TIMEOUT.reset(api_token)

    response_hash = hashlib.sha256(ham.encode("utf-8")).hexdigest()
    observed_model = metadata.get("observed_model")
    if not isinstance(observed_model, str) or not re.fullmatch(r"[A-Za-z0-9._:-]{1,128}", observed_model):
        observed_model = "unknown"
    public_meta = {
        "provider_requested": kat["saglayici"],
        "provider_observed": "unknown",
        "model_requested": kat["model"],
        "model_observed": observed_model,
        "reasoning_requested": reasoning,
        "reasoning_sent": metadata.get("reasoning_sent"),
        "reasoning_applied": "unknown",
        "reasoning_observed": "unknown",
        "compiled_message_sha256": compiled["message_sha256"],
        "request_body_sha256": metadata["request_body_sha256"],
        "response_sha256": response_hash,
    }
    def record_blocked(reason, raw):
        try:
            run.append("failed", {**public_meta, "publication": reason}, raw=raw)
        except Exception as exc:
            try:
                run.append("recovery_required", {"recording_error_type": type(exc).__name__})
            except Exception:
                pass
            raise ContextError(f"{reason}; run needs local recovery. Do not retry this call.") from None
        raise ContextError(f"{reason}; response remains private")

    if contains_secret(ham):
        record_blocked("Response matched a secret-like pattern", {"response": ham, "usage": kullanim})
    if len(ham.encode("utf-8")) > int(policy["limits"]["max_output_bytes"]):
        record_blocked("Response exceeded the policy output-byte budget", {"response": ham, "usage": kullanim})
    try:
        run.append("succeeded", public_meta, raw={"response": ham, "usage": kullanim})
    except Exception as exc:
        try:
            run.append("recovery_required", {"recording_error_type": type(exc).__name__})
        except Exception:
            pass
        raise ContextError("Provider returned; completion record needs local recovery. Do not retry this call.") from None
    print(f"Audited API call succeeded; run={run.run_id}; response remains in ignored local storage.")
    return run.run_id


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
    p.add_argument("--denetlenebilir", action="store_true", help="yalnız onaylı ve hash'li bağlamla tek API çağrısı yap")
    p.add_argument("--baglam", help="önceden derlenmiş ortak_kopru context artifact JSON dosyası")
    p.add_argument("--onay", help="derleme/politika/işlem kapsamına bağlı yerel onay dosyası")
    p.add_argument("--politika", default=os.path.join(BURASI, "policy", "policy.json"))
    a = p.parse_args()
    if a.denetlenebilir and (not a.baglam or not a.yalniz or a.kuru):
        p.error("--denetlenebilir için --baglam ve --yalniz gerekir; --kuru ile birlikte kullanılamaz")
    if a.onay and not a.denetlenebilir:
        p.error("--onay yalnız --denetlenebilir ile kullanılabilir")

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

    ayar = json.load(open(a.ayarlar, encoding="utf-8"))
    en_cok = int(ayar.get("en_cok_cikti_token", 1500))
    eklenenler = []
    for kat in ayar["katilimcilar"]:
        ad = kat["ad"]
        if a.yalniz and ad != a.yalniz:
            continue
        bek = bekleyenler(kayitlar, ad)
        if not bek:
            print(f"{ad}: bekleyen yok")
            continue
        if a.denetlenebilir:
            try:
                denetlenebilir_cagir(kat, a.baglam, a.onay, a.politika, a.dosya, a.ayarlar)
            except Exception as e:  # noqa: BLE001
                print(f"{ad}: denetlenebilir çağrı reddedildi: {e}", file=sys.stderr)
                return 2
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
