Legacy bot çağrı kayıtları uygulamanın sistem istemini, kullanıcı iletisini, ham yanıtı ve sonucu içerir. Bunlar üretici taban istemini veya tüm etkili bağlamı içermez; ham metin gizli veri taşıyabilir ve eski yolun kayıtları otomatik olarak güvenli/redakte edilmiş sayılmaz.

Yeni denetlenebilir API yolunun ham bağlamı/yanıtı varsayılan olarak yok sayılan `runs/private/` altında kalır. Bu dizin public repoya eklenmemelidir. Yayımlanan run olayları yalnız taranmış hash/metadata taşır; desen taraması eksiksiz değildir. Güven ve saklama sınırları için `../policy/README.md`.
