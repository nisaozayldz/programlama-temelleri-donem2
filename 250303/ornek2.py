urun1=int(input("ürünün fiyatını giriniz:"))
urun2=int(input("ürünün fiyatını giriniz:"))
toplam=urun1+urun2
if toplam<=200:
    print("ödenecek miktar=",toplam,"TL")
else:
    odeme=toplam*0,75
    print("ödenecek miktar",odeme)