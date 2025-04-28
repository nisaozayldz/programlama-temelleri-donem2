toplam=0
sayi1=int(input("küçük sayıyı girin"))
sayi2=int(input("büyük sayıyı girin"))
for sayi in range(sayi1,sayi2):
    if sayi %2==0:
       toplam=toplam+sayi
print("toplam değer:",toplam)