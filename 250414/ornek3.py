kenar1=int(input("kenar 1i girin:"))
kenar2=int(input("kenar 2yi girin:"))
kenar3=int(input("kenar 3ü girin:"))
if kenar1==kenar2 and kenar2==kenar3:
    print("eşkenar üçgen")
elif kenar1==kenar2 or kenar2==kenar3 or kenar1==kenar3:
    print("ikizlerkenar üçgen")
else:
    print("çeşitkenar üçgen")