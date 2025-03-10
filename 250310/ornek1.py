kilo=int(input("kg giriniz: "))
if kilo<=10:
    ucret=10*kilo
    print("ödenecek tutar",ucret)
else:
    ucret=100+(kilo-10)*7.5
    print("ödenecek tutar",ucret)