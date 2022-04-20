#FELADATON KÍVŰL
def elvalasztas():
    print("------------------------------")

feladatszam = 0

def prefix():
    return f"[{feladatszam}. Feladat]:"


"""
1.	Hozzunk létre egy üres listát „SZAMOK” néven.
"""
feladatszam = 1

szamok = []


"""
2.	Töltsük fel a listát a [10..90] zárt intervallum 3-mal osztható elemeivel.
"""
feladatszam = 2

i = 10
while (i <= 90):
    if (i % 3 == 0):
        szamok.append(i)
    i += 1

"""
3.	Írassuk ki a lista elemeit.
"""
feladatszam = 3

print(f"{prefix()}", end=" ")
print(*szamok, sep=", ")


elvalasztas()
"""
4.	Írassuk ki a lista összegét, átlagát.
"""
feladatszam = 4

osszeg = 0
i = 0
while (i < len(szamok)):
    osszeg += szamok[i]
    i += 1

db = i

atlag = osszeg / db

print(f"{prefix()} A lista összege: {osszeg}\n{prefix()} A lista átlaga: {atlag}")


elvalasztas()
"""
5.	Írassuk ki a lista páros elemeinek összegét, átlagát, darabszámát.
"""
feladatszam = 5

parosak = []

for i in szamok:
    if (i % 2 == 0):
        parosak.append(i)

parosOsszeg = 0
parosAtlag = 0
parosDb = 0

for i in szamok:
    osszeg += i
    parosDb += 1

parosAtlag = parosOsszeg / parosDb

print(f"{prefix()} A páros elemek összege: {parosOsszeg}\n{prefix()} A páros elemek átlaga: {parosAtlag}\n{prefix()} A páros elemek darabszáma: {parosDb}")


elvalasztas()
"""
6.	Válogassuk ki egy „parosak” nevű listába a páros elemeket.
"""
feladatszam = 6

#Az előző feladat így lett megoldva.


"""
7.	Válogassuk szét „kicsi” és „nagy” listába a 40 alatti és a 40 feletti elemeket.
"""
feladatszam = 7

kicsi = []
nagy = []

for i in szamok:
    if (i < 40):
        kicsi.append(i)
    else:
        nagy.append(i)


"""
8.	A „negyzetek” listába kerüljenek a „kicsi” lista elemeinek a négyzetei.
"""
feladatszam = 8

negyzetek = []

i = 0
while (i < len(kicsi)):
    if (i * i in kicsi):
        jelenlegi = []
        jelenlegi.append(i)
        jelenlegi.append(i * i)
        negyzetek.append(jelenlegi)
    i+=1

#sqrt-vel is lehetne, amihez kell importálni a math-ból.


"""
9.	Eleme-e az eredeti listának a 42? Ha igen, akkor hányadik eleme?
"""
feladatszam = 9

i = 0
index = 0
eleme = False

while (i < len(szamok)):
    if (szamok[i] == 42):
        index = i
        eleme = True
        break
    i += 1

if (eleme == True):
    print(f"{prefix()} A listának a(z) {index}. eleme a 42.")
else:
    print(f"{prefix()} A listának nem eleme a 42.")


elvalasztas()
"""
10.	Mennyi az eredeti lista páratlan elemei közül a legnagyobb, és a legkisebb?
"""
feladatszam = 10

paratlanok = []

for i in szamok:
    if (i % 2 != 0):
        paratlanok.append(i)


minParatlan = paratlanok[0]
for i in paratlanok:
    if (minParatlan > i):
        minParatlan = i

maxParatlan = paratlanok[0]
for i in paratlanok:
    if (maxParatlan < i):
        maxParatlan = i

print(f"{prefix()} A legkisebb páratlan elem: {minParatlan}\n{prefix()} A legnagyobb páratlan elem: {maxParatlan}")


elvalasztas()


#BEZÁRÁS DODGE
input("\n\n%A BEZÁRÁSHOZ NYOMJON [ENTER] BILLENTYŰT%")
