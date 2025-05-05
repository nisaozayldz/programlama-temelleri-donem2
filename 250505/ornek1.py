toplam=0
s1=int(input("küçük sayıyı girin: "))
s2=int(input("büyük sayıyı girin: "))
for sayi in range(s1,s2):
    if sayi%2==0:
        toplam=toplam+sayi
print(s1,"ile",s2,"sayıları arasındaki çift sayıların toplam:",toplam)