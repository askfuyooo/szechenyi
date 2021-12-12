#KIHÍVÁS: 23 PYTHON FELADAT 1 ÓRA ALATT.
def sortores():
    print("\n%%%%%%%%%%%%%%%%%%%%%\n")

"""
1. Írj egy Python programot, amely bekér három számot a felhasználótól és kiírja a képernyőre a
legkisebb értéket ezek közül!
"""

legkisebb = []
i = 0
while (i < 3):
    legkisebb.append(int(input(f"[1] Adja meg a {i + 1}. számot: ")))
    i+=1
print("[1] A megadott számok: ",end="")
print(*legkisebb, sep=", ")
print("[1] A legkisebb szám:", min(legkisebb))

sortores()

"""
2. Írj egy Python programot, amely bekér három számot a felhasználótól és kiírja a képernyőre a
legnagyobb értéket ezek közül!
"""

legnagyobb = []
i = 0
while (i < 3):
    legnagyobb.append(int(input(f"[2] Adja meg a {i + 1}. számot: ")))
    i+=1
print("[2] A megadott számok: ",end="")
print(*legnagyobb, sep=", ")
print("[2] A legnagyobb szám:", max(legnagyobb))

sortores()

"""
3. Írj egy Python programot, amely bekér egy dolgozat pontszámot (x) a felhasználótól és kiír egy
érdemjegyet az alábbiak szerint! 1: x<50; 2: 50<=x<60; 3: 60<=x<70; 4: 70<=x<85; 5: x>=85.
"""

jegy = 0
x = int(input("[3] Adja meg a dolgozat pontszámát: "))
if (x < 50):
    jegy = 1
elif (50 <= x < 60):
    jegy = 2
elif (60 <= x< 70):
    jegy = 3
elif (70 <= x< 85):
    jegy = 4
elif (x >= 85):
    jegy = 5

print("[3] A dolgozat pontszáma:", x, "Érdemjegye:", jegy)
sortores()

"""
4. Írj egy Python programot, amely bekér egy egész számot a felhasználótól és kiírja a képernyőre,
hogy osztható-e (igen/nem) a szám 3-mal vagy 5-tel!
"""

harom = False
ot = False

x = int(input("[4] Adjon meg egy számot: "))

if (x % 3 == 0):
    harom = True
if (x % 5 == 0):
    ot = True

if (harom == True and ot == True):
    print("[4]", x, "oszható 3-mal és 5-tel is.")
elif (harom == True and ot == False):
    print("[4]", x, "oszható 3-mal.")
elif (harom == False and ot == True):
    print("[4]", x, "oszható 5-tel.")
elif (harom == False and ot == False):
    print("[4]", x, "sem 3-mal, sem 5-tel nem osztható.")

sortores()

"""
5. Írj egy Python programot, amely bekér három számot a felhasználótól és kiírja a képernyőre,
hogy a számok közül bármelyik kettőnek az összege egyenlő-e a harmadik számmal!
"""

x = int(input("[5] Adja meg az első számot: "))
y = int(input("[5] Adja meg a második számot: "))
z = int(input("[5] Adja meg a harmadik számot: "))

if (x + y == z):
    print("[5]", x, "+", y, "=", z)
elif (x + z == y):
    print("[5]", x, "+", z, "=", y)
elif (y + z == x):
    print("[5]", y, "+", z, "=", x)
else:
    print("[5] Két szám bármelyikének összege nem egyenlő a harmadikkal.")

sortores()

"""
6. Írj egy Python programot, amely bekér három egész számot a felhasználótól és kiírja a
képernyőre, hogy mind a három páros szám-e (igen/nem)!
"""

egyparos = False
kettoparos = False
haromparos = False

x = int(input("[6] Adja meg az első számot: "))
y = int(input("[6] Adja meg a második számot: "))
z = int(input("[6] Adja meg a harmadik számot: "))

if (x % 2 == 0):
    egyparos = True
if (y % 2 == 0):
    kettoparos = True
if (z % 2 == 0):
    haromparos = True

if (egyparos == True and kettoparos == True and haromparos == True):
    print("[6]", x, y, z, "mind párosak.")
else:
    print("[6]", x, y, z, "között található páratlan.")

sortores()


"""
7. Írj egy Python programot, amely bekér két szót (sztringet) a felhasználótól és ABC sorrendben
kiírja őket a képernyőre!
"""

szavak = []
i = 0
while (i < 2):
    szavak.append(input(f"[7] Adja meg a {i + 1}. szót: "))
    i+=1
szavak.sort()

print("[7] Szavak ABC sorrendben: ", end="")
print(*szavak, sep=", ")

sortores()

"""
8. Írj egy Python programot, amely bekér egy pozitív egész számot a felhasználótól és kiírja a
képernyőre azokat a pozitív hárommal osztható számokat, amelyek kisebbek az adott számnál!
"""

x = int(input("[8] Adjon meg egy számot: "))
oszthato = []
i = 1
while (i < x):
    if (i % 3 == 0):
        oszthato.append(i)
    i+=1
oszthato.sort(reverse=True)

print("[8]", x, "-nél kisebb, 3-mal osztható számok: ", end="")
print(*oszthato, sep=", ")

sortores()

"""
9. Írj egy Python programot, amely bekér két pozitív egész számot a felhasználótól és kiírja a
képernyőre azokat a páros számokat, amelyek a két adott érték közötti zárt intervallumban
találhatóak!
"""

kezdo = int(input("[9] Adja meg a kezdőértéket: "))
veg = int(input("[9] Adja meg a végértéket: "))

intervallum = []
i = kezdo
while (i < veg):
    if (i % 2 == 0):
        intervallum.append(i)
    i+=1

print("[9]", kezdo, "és", veg, "közötti páros számok: ", end="")
print(*intervallum, sep=", ")

sortores()

"""
10. Írj egy Python programot, amely bekér egy 20-nál nem nagyobb pozitív egész számot a
felhasználótól és kiírja a képernyőre a START szót úgy, hogy előtte annyi szóköz legyen amennyi
a megadott szám értéke!
"""

siker = False
while (siker == False):
    x = int(input("[10] Adjon meg egy 20-nál kisebb számot: "))
    if (x <= 20):
        siker = True
    else:
        print(x, "nagyobb, mint 20.\n")
i = 0
while (i < x):
    print(" ", end="")
    i+=1
print("START")

sortores()

"""
11. Írj egy Python programot, amely bekér egy pozitív egész számot a felhasználótól és kiírja a
képernyőre azt a számot, amely az ennél a számnál nem nagyobb pozitív egész számok
összege!
"""

x = int(input("[11] Adjon meg egy pozitív számot: "))
i = 1
szamok = []

while (i < x):
    szamok.append(i)
    i+=1
print("[11]", x, "-nél kisebb számok darabja:", len(szamok), "összege:", sum(szamok))

sortores()

"""
12. Írj egy Python programot, amely bekér egy szót (sztringet) a felhasználótól és kiírja a
képernyőre a szó betűit, úgy, hogy minden betű egy új sorba kerüljön!
"""

szo = input("[12] Adjon meg egy szót: ")
for x in szo:
    print(x)

sortores()

"""
13. Írj egy Python programot, amely bekér egy pozitív egész számot a felhasználótól és kiírja a
képernyőre felváltva a 0 és 1 számjegyeket úgy, hogy a számjegyek együttes darabszáma
pontosan a megadott szám legyen!
"""

x = int(input("[13] Adjon meg egy pozitív számot: "))
i = 0
egyik = False

while (i < x):
    if (egyik == False):
        print("0", end="")
    else:
        print("1", end="")
    egyik = not egyik
    i+=1

print()
sortores()

"""
14. Írj egy Python programot, amely először bekér egy kisebb majd egy nagyobb pozitív valós
számot a felhasználótól és kiírja a képernyőre azokat az egész számokat, amelyek a megadott
értékek között helyezkednek el!
"""

kezdo = int(input("[14] Adjon meg egy kezdőértéket: "))
veg = int(input("[14] Adjon meg egy végértéket: "))
i = kezdo + 1
kozott = []

while (i < veg):
    kozott.append(i)
    i+=1
print("[14]", kezdo, "és", veg, "között helyezkető számok: ", end="")
print(*kozott, sep=", ")

sortores()

"""
15. Írj egy Python eljárást, amely paraméterként kap 2 egész számot (N és M) és kiír a képernyőre
a csillag (*) karaktereket M darab sorban és N darab oszlopban (tehát NxM darab karaktert egy
téglalap alakú képernyőrészre)! A programodban hívd is meg ezt az alprogramot!
"""

def csillag(oszlop, sor):
    sorok = []
    i = 0
    while (i < sor):
        sorok.append("*")
        i+=1
    i = 0
    while (i < oszlop):
        print(*sorok, sep="", end="")
        print()
        i+=1

N = int(input("Adja meg az oszlopok számát: "))
M = int(input("Adja meg a sorok számát: "))
csillag(N, M)

sortores()

"""
16. Írj egy logikai értékkel visszatérő Python függvényt, amely paraméterként kap egy egész
számot és eldönti a számról, hogy osztható-e 2-vel és 3-mal is egyszerre! A programodban hívd
is meg ezt az alprogramot!
"""

def oszthato(x):
    if (x % 2 == 0 and x % 3 == 0):
        return True
    else:
        return False

x = int(input("[16] Adjon meg egy számot: "))
if (oszthato(x) == True):
    print("[16]", x, "osztható 2-vel és 3-mal is egyszerre.")
else:
    print("[16]", x, "nem osztható 2-vel és 3-mal egyszerre.")

sortores()

"""
17. Írj egy logikai értékkel visszatérő Python függvényt, amely paraméterként kap három számot
és eldönti, hogy az összes paramétere pozitív-e! A programodban hívd is meg ezt az
alprogramot!
"""

def pozitiv(x, y, z):
    if (x >= 0 and y >= 0 and z >= 0):
        return True
    else:
        return False

x = int(input("[17] Adja meg az első számot: "))
y = int(input("[17] Adja meg a második számot: "))
z = int(input("[17] Adja meg a harmadik számot: "))

if (pozitiv(x, y, z) == True):
    print("[17]", x, y, z, "mind pozitív.")
else:
    print("[17]", x, y, z, "nem mind pozitív.")

sortores()

"""
18. Írj egy Python függvényt, amely paraméterként kap 2 egész számot és visszatér a két szám által
meghatározott zárt intervallumban található egész számok összegével! A programodban hívd
is meg ezt az alprogramot!
"""

def intervallum(K, V):
    i = K
    intervallumban = []
    while (i <= V):
        intervallumban.append(i)
        i+=1
    return sum(intervallumban)

kezdo = int(input("[18] Adja meg a kezdőértéket: "))
veg = int(input("[18] Adja meg a végértéket: "))
print("[18]", kezdo, "és", veg, "közti zárt intervallumban lévő számok összege:", intervallum(kezdo, veg))

sortores()

"""
19. Írj egy Python eljárást, amely paraméterként kap egy szót (sztringet) és annyi darab csillag (*)
karaktert ír ki a képernyőre, ahány karaktert tartalmazott a szó! A programodban hívd is meg
ezt az alprogramot!
"""

def atalakitas(szo):
    csillagok = []
    for x in szo:
        csillagok.append("*")
    print(*csillagok, sep="", end="")
    print()

sztring = input("[19] Adjon meg egy szót: ")
atalakitas(sztring)

sortores()




#Idáig jutottam 1 óra alatt. 19 feladat. További feladatokat is megoldom, de az már időn kívülre esett.
"""
20. Írj egy Python eljárást, amely paraméterként kap egy pozitív egész számot és kiír a képernyőre
ennyi karaktert úgy, hogy minden harmadik karakter pluszjel (+) legyen a többi viszont
mínuszjel (-)! A programodban hívd is meg ezt az alprogramot!
"""

def pluszminusz(szam):
    db = 1
    i = 0
    while (i < szam):
        if (db == 3):
            print("+", end="")
            db = 0
        else:
            print("-", end="")
        db+=1
        i+=1
    print()

x = int(input("[20] Adjon meg egy számot: "))
pluszminusz(x)

sortores()

"""
21. Írj egy Python programot, amely bekér a felhasználótól egy mondatot (sztringet) és ennek
szavait (szóközzel elválasztott részsztringjeit) fordított sorrendben kiírja a képernyőre!
"""

mondat = input("[21] Adjon meg egy mondatot: ").split(' ')
index = len(mondat) - 1
i = index
while (i >= 0):
    print(mondat[i], end=" ")
    i-=1

sortores()

"""
22. Írj egy Python programot, amely bekér a felhasználótól egy sztringet és ezt úgy íratja ki, hogy
a szóköz karaktereket kihagyja!
"""

mondat = input("[22] Adjon meg egy mondatot: ").split(' ')
print(*mondat, sep="")

sortores()

"""
23. Írj egy Python programot, amely a felhasználótól pozitív számokat kér be mindaddig, amíg a
felhasználó nullát nem ad be! A program az összes értéket tárolja egy listában, majd írja ki a
képernyőre a lista elemeit fordított sorrendben!
"""

szamok = []
vannulla = False
while (vannulla == False):
    x = int(input("[23] Adjon meg egy számot: "))
    if (x == 0):
        szamok.append(x)
        vannulla = True
    else:
        szamok.append(x)

szamok.sort(reverse=True)
print("[23] Számok fordított sorrendben: ", end="")
print(*szamok, sep=", ")

sortores()

#BEZÁRÁS DODGE
input("\n\n[KILÉPÉS ENTERREL]")
