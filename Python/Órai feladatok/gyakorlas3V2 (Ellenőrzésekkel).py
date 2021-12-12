"""
1. Feladat:
Írjunk olyan programot, amely számjegyenként bekér egy 3 jegyű számot,
majd kiszámolja a szám kétszeresét és kiírja a képernyőre. 
"""
lefut = False
while lefut == False:
    try:
        x = int(input("Adja meg a háromjegyű szám első számjegyét: "))
        if x < 10 and x >= 0 and x != 0:
            lefut = True
        else:
            print("Az első számjegy nem lehet 0. A szám nem lehet negatív és/vagy nagyobb, mint 9!\n")
    except:
        print("Igazi számot adjon meg!\n")

lefut = False
while lefut == False:
    try:
        y = int(input("Adja meg a háromjegyű szám második számjegyét: "))
        if y < 10 and y >= 0:
            lefut = True
        else:
            print("A szám nem lehet negatív és/vagy nagyobb, mint 9!\n")
    except:
        print("Igazi számot adjon meg!\n")

lefut = False
while lefut == False:
    try:
        z = int(input("Adja meg a háromjegyű szám harmadik számjegyét: "))
        if z < 10 and z >= 0:
            lefut = True
        else:
            print("A szám nem lehet negatív és/vagy nagyobb, mint 9!\n")
    except:
        print("Igazi számot adjon meg!\n")

x = x * 100
y = y * 10
szam = x + y + z
print("A bekért szám:", szam, "kétszerese:", szam*2, "\n")



"""
2. Feladat:
Írjunk olyan programot,
amely számjegyenként bekér egy 4 jegyű kettes számrendszerben felírt számot,
majd átváltja a számot tízes számrendszerbe.
"""
szamrendszer = []
i = 0
while i < 4:
    kiiras = "Adjon meg egy kettes számrendszerben felírt szám {0}. számjegyét: ".format(i + 1)
    lefut = False
    while lefut == False:
        try:
            x = int(input(kiiras))
            if x == 0 or x == 1:
                szamrendszer.append(x)
                lefut = True
            else:
                print("A kettes számrendszerben csak 0 és 1 található.")
        except:
            print("Igazi számot adjon meg.")
    i+=1

szam = 0
if szamrendszer[3] == 1:
    szam+=1
if szamrendszer[2] == 1:
    szam+=2
if szamrendszer[1] == 1:
    szam+=4
if szamrendszer[0] == 1:
    szam+=8
print("A kettes számrendszerbéli szám: ", end="")
print(*szamrendszer, sep="", end="")
print("\nÁtváltva:", szam)


#BEZÁRÁS DODGE
input("KILÉPÉSHEZ NYOMJON [ENTER]-T!")
