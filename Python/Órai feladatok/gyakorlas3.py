"""
1. Feladat:
Írjunk olyan programot, amely számjegyenként bekér egy 3 jegyű számot,
majd kiszámolja a szám kétszeresét és kiírja a képernyőre. 
"""
x = int(input("Adja meg a háromjegyű szám első számjegyét: "))
y = int(input("Adja meg a háromjegyű szám második számjegyét: "))
z = int(input("Adja meg a háromjegyű szám harmadik számjegyét: "))

x = x * 100
y = y * 10
szam = x + y + z
print("A bekért szám:", szam, "kétszerese:", szam*2)

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
    szamrendszer.append(int(input(kiiras)))
    i+=1

#0101
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
