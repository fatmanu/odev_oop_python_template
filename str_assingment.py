'''
YBS401-2021-fall-2
Ödev kapsamında yapmanız gereken:
aşağıdaki fonksiyonların içeriklerini düzeltmenizdir.
hazırlayan @aucan

Öğrenci Ad Soyad=
Öğrenci No=
Bölüm=
Sınıf=
'''

def format_string():
    '''
    Fonksiyonun geri dönüş değeri 
    "Adı:Ali,Soyadı:Yılmaz,Yaşı:20"
    olacak şekilde eksik kısımları doldurmanızdır. (1 puan)
    Sadece #------**------ işareti ile belirtilen 
    kısımlar arasını değiştiriniz. 

    text değişkenini string format fonksiyonu ile doldurmanız beklenmektedir.
    '''
    name = "Ali"
    surname = "Yılmaz"
    birth = 2001
    #-------**-----------
    #kodunuzu bu yorum satırını silerek buraya yazınız, diğer kısımları değiştirmeyiniz.
    #-------**-----------
    return text


def concat_string():
    '''
    Fonksiyonun geri dönüş değeri 
    "29 Ekim Cumhuriyet Bayramımız Kutlu Olsun!"
    olacak şekilde eksik kısımları doldurmanızdır. (1 puan)
    Sadece #------**------ işareti ile belirtilen 
    kısımlar arasını değiştiriniz. 

    text değişkeni içerisini str1 str2 str3 değişkenlerini uygun hale getirip birleştirerek doldurmanız beklenmektedir.
    Küçük BÜYÜK harfe, boşluklara, str+number hatasına ve birleştirme sırasına dikkat ediniz.
    '''
    str1 = "  kutlu olsun!          "
    str2 = "    ekim cumhuriyet bayramımız    "
    str3 = 29
    #-------**-----------
    #kodunuzu bu yorum satırını silerek buraya yazınız, diğer kısımları değiştirmeyiniz.
    #-------**-----------
    return text


def slice_string():
    '''
    Fonksiyonun geri dönüş değeri 
    "deF!N!567%&/_"
    olacak şekilde eksik kısımları doldurmanızdır. (1 puan)
    Sadece #------**------ işareti ile belirtilen 
    kısımlar arasını değiştiriniz. 

    text değişkeni içerisini numbers aplhabets signs değişkenlerini uygun hale getirip birleştirerek doldurmanız beklenmektedir.
    Küçük BÜYÜK harfe ve birleştirme sırasına dikkat ediniz.
    Slicing Strings bölümünde öğrendiğiniz gibi yapmanız gerekmektedir. 
    örneğin "ABC012.," için 
    text = alphabets[0:3] + numbers[0:3] + signs[0:2] 
    '''
    numbers = "0123456789"
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    signs = ".,!'^+$%&/()=?*-_"
    #-------**-----------
    #kodunuzu bu yorum satırını silerek buraya yazınız, diğer kısımları değiştirmeyiniz.
    #-------**-----------
    return text



def replace_string():
    '''
    Fonksiyonun geri dönüş değeri 
    "Korkut Ata Üniversitesi bölgenin en iyisidir."
    olacak şekilde eksik kısımları doldurmanızdır. (1 puan)
    Sadece #------**------ işareti ile belirtilen 
    kısımlar arasını değiştiriniz. 

    text değişkeni içerisini first_text,searchv,replacev değişkenlerini uygun hale getirip doldurmanız beklenmektedir.
    Küçük BÜYÜK harfe dikkat ediniz.
    Replace Strings bölümünde öğrendiğiniz gibi yapmanız gerekmektedir.  
    '''
    first_text = "Çukurova Üniversitesi bölgenin en iyisidir." #orjinal metin
    searchv = "çukurova" #aranan ifade
    replacev = "korkut ata" #değişecek ifade
    #-------**-----------
    #kodunuzu bu yorum satırını silerek buraya yazınız, diğer kısımları değiştirmeyiniz.
    #-------**-----------
    return text

