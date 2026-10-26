# Üretici adresi ve açık katman adresi

Bir kaydın alıcısı ChatGPT (Şaman) ise, ChatGPT (API) yanıtı bu işi kapsamaz. CLI yolu bulunamadığında veya hata verdiğinde, API yedeği bu katman işini devralmaz. Her yol kendi imzasıyla bekleyenleri yeniden seçer; API yedeğine üst CLI'ın imzası aktarılmaz.

Yalın ChatGPT, Claude, Copilot ve Gemini adresleri eski üretici adresleridir. Bu kayıtların geçmiş kapsama davranışı korunur; eski işler yeniden açılmaz. Aynı kayıtta açık katman ile yalın üretici birlikte adreslenmişse, ilgili kapsamlar ayrı değerlendirilir. Yanıtın kapsadığı üst kayıt numarası yalnız o hedef kapsamı için geçerlidir.

Şaman/Saman → ChatGPT (Şaman), Hacker → Claude (Hacker) takma adları desteklenir. Şahit’in güncel rol adı Gemini (Şahit) olarak kaydedilmiştir; mevcut kodun tarihsel Şahit/Sahit takma adı ise Copilot (Şahit) adresine bağlıdır. Eski kayıtları başka üreticiye yönlendirmemek için bu eşleme korunur. Yeni işler açıkça Gemini (Şahit) olarak adreslenmelidir; Google (CLI izleyici) de ayrı bir adrestir ve bu imzaların yerine geçmez. API yolları bu CLI imzalarını kullanamaz. CLI ayarlarında doğru imza açıkça verilmelidir; eksik CLI imzasının varsayılanı üretici (CLI) olur, başka rol tahmin edilmez.

    python kopru_yanitla.py kopru.html --bekleyenler "ChatGPT (Şaman)"
    python kopru_yanitla.py kopru.html --istem "Gemini (Şahit)"

Hedefleme regresyonları; açık katman, API/CLI yanıt ayrımı, eski üretici adresleri, takma adlar, API yedeğinin yeniden seçimi ve kuru çalıştırmada çağrı/yazım olmamasını sınar. İlk hedefleme düzeltmesindeki salt okunur karşılaştırmada üç CLI yolunun bekleyenleri önce/sonra sıfırdı; bu tarihsel sonuç güncel kuyruk sayısı değildir. Regresyonlar model, API veya CLI iş çağrısı yapmaz; Google, Gemini ve Copilot kimliklerinin ayrılığını da sınar.

    python -m unittest discover -s tests -p test_katman_hedefleme.py -v

Bu sözleşme kayıt ve yapılandırma hedefini ayırır. Bir imza, katmanın gerçekten okuduğunun veya belirli açık oturumun yanıtladığının kanıtı değildir. Belirli oturum teslimi deus_ex_machina yüzeyinde ayrı oturum anahtarı, gerçek alım ve yanıt kaydıyla izlenir.
