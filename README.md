# Web-Indexleme-Uygulamasi
Verilen bir URL’deki web sayfa içeriğine göre sayfada geçen kelimelerin frekanslarının hesaplanması, anahtar kelimelerin çıkarılması, iki sayfa arasındaki benzerlik skorlamasının hesaplanması, diğer birden  fazla web sayfasını benzerlik bakımından indeksleyip sıralayan web tabanlı bir uygulama geliştirilmesi ve verilen web siteleri içindeki anahtar kelimelerle semantik analiz tespiti yapılması hedeflenmiştir. Böylece bu proje sayesinde web indeksleme yöntemleri hakkında bilgi edinilmesini ve web tabanlı  uygulama yazma becerisinin geliştirilmesi amaçlanmaktadır..

Python ve HTML dilleri kullanıldı.

**1. Sitemiz nasıl çalışır?**
1.‘templates’ klasörüne girin ve ‘GIRIS.html’ dosyası açınız.
2. “Proje” butona basınız.
**! DIKKAT:** “Frekans”, “Anahtar Kelimeler” ve “Site İndexleme” sizin seçtiğiniz web sayfasına göre 
çalışması için ‘yaz_lab_1.py’ dosyası açmanız lazım ve ‘url_1’ değiştirmeniz gerekecektir.
3. Sayfada Geçen Kelimelerin Frekanslarını görebilmek için menüden “Frekans” seçiniz.
4. Anahtar Kelimeri görebilmek için menüden “Anahtar Kelimeler” seçiniz.
5. Site İndexleme ve Sıralama görebilmek için menüden “Indexleme” seçiniz.
6. İki Sayfa (URL) Arasındaki Benzerlik Skorlaması görebilmek için menüden “Benzerlik” seçiniz.
**! DIKKAT:** “Benzerlik” çalışması için iki tane URL link gereklidir. Sizin seçtiğiniz web sayfalarına 
göre çalışması için ‘yaz_lab_1.py’ dosyasında ‘url_1’ ve ‘3Asama.py’ dosyasında ‘url_2’ 
değiştirmeniz gerekecektir. Eğer ‘url_1’ değiştirmezsiniz o zaman “Frekans” için kullandığınız siteyi 
ve yeni olan ‘url_2’ siteyi göre Benzerlik Testi uygulanacaktır!

o Python BeautifulSoup Modülü
BeautifulSoup, HTML veya XML dosyalarını işlemek için oluşturulmuş güçlü ve hızlı bir 
kütüphanedir. Bu modül ile bir kaynak içerisindeki HTML kodlarını parse edip,botlar 
yazabiliriz.
• Peki onu ne için kullandık?
Verilern URL açmak ve o sayfadaki verileri okumak için kullandık.
o Requests modülü
Bu modül ile web üzerindeki isteklerinizi yöneteceksiniz. Mesela bu modül ile API 
entpointlerine PUT, DELETE, POST gibi istekler atabilirsiniz.
• Ne için kullandık?
Projenin web sitesindeki ilk sayfada URL girilecek alanı oluşturduk.POST ve GET 
metodlarını da kullandık fakat kodumuzu çalıştıramadık.
o Collections modülü
Koleksiyon modülü, Python'da yerleşik bir modüldür. Sözlük, liste, küme ve tuple gibi temel 
veri türlerinin aksine özel kap veri türlerini uygular.
• Ne için kullandık?
2.Asamada Anahtar kelimeleri bulabilmek için kullandık.
o Flask modülü
Flask bir python frameworküdür. Web servislerinde de hızlı sonuç elde etmek için pythonun 
flask frameworkünden yararlanılabilir.
