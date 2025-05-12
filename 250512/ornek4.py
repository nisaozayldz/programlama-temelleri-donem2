notlar=[]
zayif_sayisi=0
for i in range(6):
    notlar.append(int(input("not girin: ")))
for j in notlar:
    toplam=toplam+j
if j<50:
    zayif_sayisi=zayif_sayisi+1