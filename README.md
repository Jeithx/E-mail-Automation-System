# E-posta Otomasyon Sistemi

Bu proje, kullanıcıların toplu e-posta göndermesini sağlayan bir otomasyon sistemidir. Kullanıcılar, alıcıların isimlerini ve e-posta adreslerini girerek, belirli bir konu ve içerik ile toplu e-posta gönderebilirler. Proje, PyQt5 kullanarak bir masaüstü uygulaması oluşturmuştur ve SMTP üzerinden e-posta göndermektedir.

## Özellikler

- **SMTP ile e-posta gönderimi:** Gmail SMTP sunucusu kullanılarak e-posta gönderimi yapılır.
- **Toplu E-posta Gönderimi:** Birden fazla alıcıya kişiselleştirilmiş e-posta gönderimi.
- **E-posta İçeriği Kişiselleştirme:** E-posta içeriği, her alıcıya özel bir "Merhabalar! {isim}" ile kişiselleştirilir.
- **E-posta Formatı Doğrulaması:** E-posta adresleri basit bir regex ile doğrulanır.
- **Hatalı E-posta Adresleri Bilgisi:** Hatalı e-posta adresleri ekranda gösterilir.

## Kullanım

### Gereksinimler

Bu uygulamayı çalıştırabilmek için Python ve aşağıdaki bağımlılıkların yüklü olması gerekmektedir:

- Python 3.x
- PyQt5
- smtplib (Python standart kütüphanesi ile birlikte gelir)

### Kurulum

1. Bu projeyi GitHub'dan klonlayın:

   ```bash
   git clone https://github.com/kullaniciadi/email-otomasyon-sistemi.git
