sure=int(input("süreyi giriniz:"))
if sure<=60:
    print("ücret:5tl")
elif sure <=300:
    print("ücret:"+str((sure/60)*4)+"TL")
else:
    print("ücret:"+str((sure/60)*3)+"TL")