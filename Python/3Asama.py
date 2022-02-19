#Import libraries(kütüphaneler)
from urllib.request import urljoin
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

import math
import string
import sys



url_2 = "https://www.kariyer.net/pozisyonlar/bilgisayar+muhendisi/nedir"
url_2_open = urlopen(url_2).read()
soup = BeautifulSoup(url_2_open, features="html.parser")

# script ve style varsa onlara cikar
for script in soup(["script", "style"]):
    script.extract()  

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
dosya_web_2 = open('webSayfa_txtDosya_2.txt', 'w')
print(text.encode("utf-8"), file=dosya_web_2)
# dosyayi kapat
dosya_web_2.close()


#-----------------------------------------------------------------------
# fonksiyon - Frekans bulmak
def frekans(str): 
  
    # str'ten kelimeler 
    str_list = str.split() 
  
    # benzersiz kelimeler 
    unique_words = set(str_list) 
      

    dosya = open('3asamaKelimeler_2.txt', 'w', encoding='utf-8')
    for words in unique_words : 
        print(words, file=dosya)
    dosya.close()


#-----------------------------------------------------------------------
# fonksiyon - .txt oku
def dosya_oku(dosya_ismi):
    
    try:
        with open(dosya_ismi, 'r', encoding='utf-8') as d:
            data = d.read()
        return data
    
    except IOError:
        print("HATA! ", dosya_ismi)
        sys.exit()


# Metin satırlarını kelimelere bölme,
# büyük harfleri küçük harfe yap, 
tablo_cevir = str.maketrans(string.punctuation+string.ascii_uppercase,
                                    " "*len(string.punctuation)+string.ascii_lowercase)
   

#----------------------------------------------------------------------- 
# fonksiyon - kelimeler
def satirlardan_kelime_al(text):
    
    text = text.translate(tablo_cevir)
    kelime_liste = text.split()
    
    print(kelime_liste)
    return kelime_liste


#-----------------------------------------------------------------------
# fonksiyon - Frekans bul
def frekans_bul(kelime_liste):
    
    K = {}
    
    for kelime_yeni in kelime_liste:
        
        if kelime_yeni in K:
            K[kelime_yeni] = K[kelime_yeni] + 1
            
        else:
            K[kelime_yeni] = 1
            
    return K

# .txt dosyayi ac ('a' -> yazdir(üzerine yazmak yerine ekleme),
# Karakter Kodlama(utf-8 -> butun diller icin kullanabilir))
dosya_asama_3_sonuc = open('asama_3.txt', 'a', encoding='utf-8')


#-----------------------------------------------------------------------
# fonksiyon - (kelime, frekans) döndürür
def frekans_kelime_dosyada(dosya_ismi):
    
    #
    satir_liste = dosya_oku(dosya_ismi)
    #
    kelime_liste = satirlardan_kelime_al(satir_liste)
    #
    farkli_liste = frekans_bul(kelime_liste)
    
    print("-----------------------------")
    print("Dosya", dosya_ismi, ":", )
    print(len(satir_liste), "Satır, ", )
    print(len(kelime_liste), "Kelime, ", )
    print(len(farkli_liste), "Farklı Kelime")
    
    print("-----------------------------", file=dosya_asama_3_sonuc)
    print("Dosya", dosya_ismi, ":", file=dosya_asama_3_sonuc )
    print(len(satir_liste), "Satır, ", file=dosya_asama_3_sonuc )
    print(len(kelime_liste), "Kelime, ", file=dosya_asama_3_sonuc )
    print(len(farkli_liste), "Farklı Kelime", file=dosya_asama_3_sonuc)    

    return farkli_liste


#-----------------------------------------------------------------------
# fonksiyon - iki belgenin iç çarpımını döndür
def icCarpi(K1, K2):
    Toplam = 0.0
    
    for c in K1:
        
        if c in K2:
            Toplam += (K1[c] * K2[c])
            
    return Toplam


#-----------------------------------------------------------------------
# belge vektörleri arasındaki açıyı radyan cinsinden döndür
def aci(K1, K2):
    ilk = icCarpi(K1, K2)
    sonra = math.sqrt(icCarpi(K1, K1)*icCarpi(K2, K2))
    
    return math.acos(ilk / sonra)


#-----------------------------------------------------------------------
# fonksiyon - Benzerlik Skorlamasi
def benzerlikSkorlamasi(dosya_ismi_1, dosya_ismi_2):
    sorted_word_list_1 = frekans_kelime_dosyada(dosya_ismi_1)
    sorted_word_list_2 = frekans_kelime_dosyada(dosya_ismi_2)
    benzerlik = aci(sorted_word_list_1, sorted_word_list_2)
    
    print("BENZERLIK Skorlaması: % 0.6f (radians)"% benzerlik, file=dosya_asama_3_sonuc)
    

# calistir
benzerlikSkorlamasi('3asamaKelimeler.txt', '3asamaKelimeler_2.txt')

# dosyayi kapat
dosya_asama_3_sonuc.close()

#txt(frekans) html e
dosya_asama_3 = open('asama_3.txt', 'r')
with open("templates/benzerlik.html", "w") as e:
    for satirlar in dosya_asama_3.readlines():
        e.write("<pre>" + satirlar + "</pre> <br>\n")



#-----------------------------------------------------------------------
# MAIN
if __name__ == "__main__":
    str =text
      
    # frekans fonksiyonu cagir 
    frekans(str)