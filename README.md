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
2. Bağımlılıkları yükleyin:
   
   ```bash
   pip install pyqt5

3. main.py dosyasını çalıştırarak uygulamayı başlatın:

   ```bash
   python main.py

## Uygulama Kullanımı

- Gönderen E-posta Adresi ve Şifresi: E-posta adresinizi ve şifrenizi girin. (Gmail kullanıyorsanız, güvenlik nedeniyle "Daha Az Güvenli Uygulamalar" seçeneğini açmanız gerekebilir.)
- Konu ve İçerik: Göndereceğiniz e-posta'nın konusu ve içeriğini yazın.
- Alıcılar: Alıcıların isimlerini ve e-posta adreslerini tabloya ekleyin. Her alıcı için bir satır ekleyebilirsiniz.
- E-posta Gönderimi: "E-posta Gönder" butonuna tıklayarak toplu e-posta gönderebilirsiniz.
- Sonuçlar: Başarıyla gönderilen e-posta sayısı ve hatalı e-posta adresleri ekranda gösterilecektir.

## Katkıda Bulunma
- Bu projeye katkıda bulunmak isterseniz, lütfen bir pull request gönderin.
- İssues bölümünden hata bildirebilir veya geliştirme önerilerinde bulunabilirsiniz.

## Lisans
- Bu proje GNU Lisansı altında lisanslanmıştır.

## İletişim
-Bu proje hakkında daha fazla bilgi almak isterseniz, email@example.com adresinden benimle iletişime geçebilirsiniz.




