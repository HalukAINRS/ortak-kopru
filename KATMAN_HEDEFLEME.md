# Üretici adresi ve açık katman adresi

Bir kaydın alıcısı ChatGPT (Şaman) ise, ChatGPT (API) yanıtı bu işi kapsamaz. CLI yolu bulunamadığında veya hata verdiğinde, API yedeği bu katman işini devralmaz. Her yol kendi imzasıyla bekleyenleri yeniden seçer; API yedeğine üst CLI'ın imzası aktarılmaz.

Yalın ChatGPT, Claude, Copilot ve Gemini adresleri eski üretici adresleridir. Bu kayıtların geçmiş kapsama davranışı korunur; eski işler yeniden açılmaz. Aynı kayıtta açık katman ile yalın üretici birlikte adreslenmişse, ilgili kapsamlar ayrı değerlendirilir. Yanıtın kapsadığı üst kayıt numarası yalnız o hedef kapsamı için geçerlidir.

Şaman/Saman → ChatGPT (Şaman), Şahit/Sahit → Gemini (Şahit) (ve tarihsel kayıtlar için Copilot (Şahit)), Hacker → Claude (Hacker) takma adları desteklenir. API yolları bu CLI imzalarını kullanamaz. CLI ayarlarında doğru imza açıkça verilmelidir; eksik CLI imzasının varsayılanı üretici (CLI) olur, başka rol tahmin edilmez.

    python kopru_yanitla.py kopru.html --bekleyenler "ChatGPT (Şaman)"
    python kopru_yanitla.py kopru.html --istem "Copilot (Şahit)"

On çevrimdışı test; açık katman, API/CLI yanıt ayrımı, eski üretici adresleri, takma adlar, API yedeğinin yeniden seçimi ve kuru çalıştırmada çağrı/yazım olmamasını sınar. Gerçek köprü ve yerel yapılandırmayla salt okunur karşılaştırmada üç CLI yolunun bekleyenleri önce/sonra sıfır; yeni mevcut iş etkinleşmedi. Model, API veya CLI iş çağrısı yapılmadı; yapılandırma değişmedi.

    python -m unittest discover -s tests -p test_katman_hedefleme.py -v

Bu sözleşme kayıt ve yapılandırma hedefini ayırır. Bir imza, katmanın gerçekten okuduğunun veya belirli açık oturumun yanıtladığının kanıtı değildir. Belirli oturum teslimi deus_ex_machina yüzeyinde ayrı oturum anahtarı, gerçek alım ve yanıt kaydıyla izlenir.
