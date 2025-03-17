adet=int(input("kaç tane alacaksınız: "))
fiyat=int(input("ürünün fiyatını girin: "))
toplam=adet*fiyat
if toplam>=3000:
    toplam=toplam-0.20
    print("ürünlerin tutarı:",toplam)
else:
    toplam=toplam-100
    print("ürünlerin tutarı:",toplam)