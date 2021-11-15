'''
YBS401-2021-fall-2
Ödev kapsamında yapmanız gereken:

Oncelikle urunler adinda bir sinif tanimlayiniz. 
Urunler sinifi urun_adi, urun_alis_fiyati, urun_otv_orani, urun_kdv_orani ozelliklerine sahip olmalidir. 
Urunler sinifi constructor kullanmalidir. Constructor içerisine sirayla
urun_adi, urun_alis_fiyati, urun_otv_orani, urun_kdv_orani parametre olarak almalidir. 
Urunler sinifi urun_satis_fiyati() adında bir methoda sahip olmalıdır. 
urun_satis_fiyati() methodu kar_orani parametresine sahip olmalidir. 
urun_satis_fiyati() methodu urunun karli ve vergilendirilmis fiyatini hesaplayarak dondurmelidir. 
urun fiyati hesaplarken once kar sonra otv ve kdv sirayla alis fiyatina eklenmelidir. 



hazırlayan @aucan

Öğrenci Ad Soyad=Fatma Nur Özkan
Öğrenci No=2018507044
Bölüm=YBS
Sınıf= 4
'''

class urunler:
    urun_adi = -
    urun_alis_fiyati = -
    urun_otv_orani = 0
    urun_kdv_orani =0
    
    def __init__ (self,aurun_adi,aurun_alis_fiyati,aurun_otv_orani,aurun_kdv_orani):
          
          self.urun_adi = aurun_adi
          self.urun_alis_fiyati = aurun_alis_fiyati
          self.urun_otv_orani.  = aurun_otv_orani
          self.urun_kdv_orani   = aurun_kdv_orani
    
    def urun_satis_fiyati(self,kar_orani):
    
          self.urun_alis_fiyati = self.urun_alis_fiyati + (self.urun_alis_fiyati * kar_orani):
          self.urun_alis_fiyati = self.urun_alis_fiyati + (self.urun_alis_fiyati * self.urun_satis_fiyati):
          self.urun_alis_fiyati = self.urun_alis_fiyati + (self.urun_alis_fiyati * self.urun_satis_fiyati):
          return self.urun_alis_fiyati
    
def sepet_fiyati(kar_orani):
    '''
    Fonksiyon urunlerin toplam fiyatini geri dönüş değeri olarak dondurmelidir. (5 puan)
    Sadece #------**------ işareti ile belirtilen 
    kısımlar arasını değiştiriniz. 

    toplam değişkenini doldurmanız beklenmektedir.
    '''
    ekmek=urunler('ekmek',1,0.20,0.12)
    patates=urunler('patates',2,0.16,0.18)
    elma=urunler('elma',3,0.11,0.22)
    un=urunler('un',4,0.17,0.05)
    yumurta=urunler('yumurta',5,0.30,0.19)
    toplam=0   
    #-------**-----------
    #kodunuzu bu yorum satırını silerek buraya yazınız, diğer kısımları değiştirmeyiniz.
    #-------**-----------
    return toplam


def odev_test():
    sepet_toplam = sepet_fiyati(0.15)
    if sepet_toplam==23.91218:
        print("doğru")
    else:
        print("yanlış")


#bu test methodunu kullanarak yazdığınız kodu test edebilirsiniz
odev_test()
