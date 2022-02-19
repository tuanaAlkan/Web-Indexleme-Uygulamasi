#Import libraries(kütüphaneler)
from urllib.request import urljoin
import requests
from urllib.request import urlparse
# Bu modül ile web üzerindeki isteklerimizi yönetecegiz
import requests
from flask import Flask, redirect, url_for, render_template
import re, operator
# HTML veya XML dosyalarını işlemek için oluşturulmuş güçlü ve hızlı bir kütüphanedir
from bs4 import BeautifulSoup
from urllib.request import urlopen
# liste, set, tuple vb. gibi veri koleksiyonlarını depolamak için kullanılır
import collections

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("home.html")


url_1 = "https://www.kariyer.net/pozisyonlar/bilgisayar+muhendisi/nedir"
url_1_open = urlopen(url_1).read()
soup = BeautifulSoup(url_1_open, features="html.parser")

# script ve style varsa onlara cikar
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# text al
text = soup.get_text()

# satırlara böl ve her boşluklari kaldırın (başındaki ve sonundaki)
satirlar = (satir.strip() for satir in text.splitlines())
# çoklu başlıkları varsa her birini bir satıra ayırın
bosluklar = (phrase.strip() for satir in satirlar for phrase in satir.split("  "))
# bos satırlar bırak
text = '\n'.join(bosluk for bosluk in bosluklar if bosluk)

#ciktisi yazdir 
print(text)

# .txt dosyasina yazdir
# .txt dosyayi ac ('w' -> yazdir)
dosya_web_1 = open('webSayfa_txtDosya.txt', 'w')
print(text.encode("utf-8"), file=dosya_web_1)
# dosyayi kapat
dosya_web_1.close()


#-----------------------------1 ASAMA------------------------------------------
# Sayfada Geçen Kelimelerin Frekanslarını Hesaplama  
# fonksiyon - Frekans bulmak
def frekans(str): 
  
    # str'ten kelimeler  
    str_list = str.split() 
  
    # benzersiz kelimeler  
    unique_words = set(str_list) 
      
    for words in unique_words : 
        print(words , ': ', str_list.count(words)) 

    #frekans to .txt
    dosya_asama_1 = open('asama_1.txt', 'w', encoding='utf-8')
    for words in unique_words : 
        print(words , ': ', str_list.count(words), file=dosya_asama_1)
    dosya_asama_1.close()

    dosya_asama_3_1 = open('3asamaKelimeler.txt', 'w', encoding='utf-8')
    for words in unique_words : 
        print(words, file=dosya_asama_3_1)
    dosya_asama_3_1.close()

#txt(frekans) html e
dosya_asama_1_r = open('asama_1.txt', 'r')
with open("templates/frekans.html", "w") as e:
    for lines in dosya_asama_1_r.readlines():
        e.write("<pre>" + lines + "</pre> <br>\n")


#-----------------------------2 ASAMA------------------------------------------
# Anahtar Kelime Çıkarma 
def anahtar_kelime(str):
    counts = collections.Counter(str.split())
    # counts.most_common(5)
    print("----------------------------------------") 
    print(counts.most_common(5)) 
    print("----------------------------------------") 

    #anahtar kelime to .txt
    dosya_asama_2 = open('asama_2.txt', 'w', encoding='utf-8')
    print(counts.most_common(5), file=dosya_asama_2)
    dosya_asama_2.close()

#txt(anahtarKelimeler) html e
dosya_asama_2_r = open('asama_2.txt', 'r')
with open("templates/anahtarKelimeler.html", "w") as e:
    for lines in dosya_asama_2_r.readlines():
        e.write("<pre>" + lines + "</pre> <br>\n")


#-----------------------------4 ASAMA------------------------------------------
# Site İndexleme ve Sıralama 
# ic baglanti 
ic_baglanti = set()
url_asama_4 = "https://garson3d.wordpress.com/"
# 4 asamada soyledigi 3 seviye, bizim 2 seviyesi esittir(0 dan basladik)
seviye = 2
  
# dis baglanti
dis_baglanti = set()
  

# fonksiyon - sitenin seviyesi bulmak
def site_seviye(url_asama_4):
    url_gecici = set()
    url_simdiki = urlparse(url_asama_4).netloc
  
    # Html etiketlerini çıkarmak için beautiful_soup_object nesnesi oluşturur
    beautiful_soup_object = BeautifulSoup(
        requests.get(url_asama_4).content, "lxml")
  
    # butun html linkleri cikar ve onlar ayril(ic ve dis baglantilari olarak)
    for anchor in beautiful_soup_object.findAll("a"):
        href = anchor.attrs.get("href")
        if(href != "" or href != None):
            href = urljoin(url_asama_4, href)
            href_parsed = urlparse(href)
            href = href_parsed.scheme
            href += "://"
            href += href_parsed.netloc
            href += href_parsed.path
            final_parsed_href = urlparse(href)
            gecerli_mi = bool(final_parsed_href.scheme) and bool(
                final_parsed_href.netloc)
            if gecerli_mi:
                if url_simdiki not in href and href not in dis_baglanti:
                    print("[!] Dış Bağlantı: {}".format(href), file=dosya_asama_4)
                    dis_baglanti.add(href)
                if url_simdiki in href and href not in ic_baglanti:
                    print("[*] Dahili Bağlantı(İç Link): {}".format(href), file=dosya_asama_4)
                    ic_baglanti.add(href)
                    url_gecici.add(href)
    return url_gecici
  
#anahtar kelime to .txt
dosya_asama_4 = open('asama_4.txt', 'w', encoding='utf-8')
print("1.Seviye", file=dosya_asama_4)
print("[ ] Giriş Sayfa: {}".format(url_asama_4), file=dosya_asama_4)

# eger seviye = 0 ise
if(seviye == 0):
    print("[ ] Giriş Sayfa: {}".format(url_asama_4), file=dosya_asama_4)

#eger seviye = 1 ise
elif(seviye == 1):
    level_crawler(url_asama_4)
    
# farkli sevie ise
else:
    # BFS kullandik (agac olarak)
    kuyruk = []
    kuyruk.append(url_asama_4)
    print("2.Seviye", file=dosya_asama_4)
    
    for j in range(seviye):
        print("3.Seviye ", file=dosya_asama_4)
        for count in range(len(kuyruk)):
            url = kuyruk.pop(0)
            
            urls = site_seviye(url)
            for i in urls:
                kuyruk.append(i)
# dosyayi kapat
dosya_asama_4.close()

#txt(anahtarKelimeler) html e
dosya_asama_4_r = open('asama_4.txt', 'r')
with open("templates/siteIndexleme.html", "w") as e:
    for lines in dosya_asama_4_r.readlines():
        e.write("<pre>" + lines + "</pre> <br>\n")


#-----------------------------MAIN------------------------------------------
if __name__ == "__main__":
    str =text
    # frekans fonksiyonu cagir
    frekans(str)
    # anahtar_klime fonksiyonu cagir 
    anahtar_kelime(str)
    #calistir
    app.run(debug=True)

