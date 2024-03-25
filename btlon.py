def nhapthongtin():
    dk1=dk2=dk3=dk4=0
    while True:
        if dk1==0:
            shp=input("moi nhap so hieu phong: ")
            if len(shp):
                dk1=1
        if dk2==0:
            shtn=input("moi nhap so hieu toa nha: ")
            if len(shtn):
                dk2=1
        if dk3==0:
            tch=input("moi nhap ten chu ho: ")
            if len(tch):
                dk3=1
        if dk4==0:
            try:
                sokW=input("moi nhap so kW: ")
                if len(sokW):
                    dk4=1
            except:
                print("ban da nhap sai thong tin")
        if dk1==dk2==dk3==dk4==1:
            sokW = int(sokW)  # Convert sokW to an integer
            td = tinhtiendiensauthue(sokW)
            return " phong: " + shp + "toa nha" + shtn + " ten: " + tch + "so kW: " + str(sokW) + " tong: "+ str(td)

def tinhtiendien(soKW):
    if soKW <= 100:
        return soKW * 1450
    elif soKW <= 150:
        return soKW * 1450 + (soKW-100)*1750
    elif soKW <= 250:
        return 100 * 1450 + 50 * 1750 + (soKW-150)*2000
    else:
        return 100 * 1450 + 50 * 1750 + 100 * 2000 + (soKW-250)*2500  

def tinhtiendiensauthue(soKW):
    return tinhtiendien(soKW)*11/10

def ghithongtin(thongtin):
    try:
        f = open("toannha.txt","a")
        f.write(thongtin)
        f.close()
    except:
        print("file co van de")

ghithongtin(nhapthongtin())
