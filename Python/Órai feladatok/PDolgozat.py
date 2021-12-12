"""
1.	Hozzunk létre egy üres listát „dolgozat” néven.
"""
dolgozat = []
"""
2.	Töltsük fel a listát a [30..50] zárt intervallum 3-mal osztható elemeivel.
"""
i = 30
while (i < 50):
    if (i % 3 == 0):
        dolgozat.append(i)
    i+=1
"""
3.	Írassuk ki a lista elemeit.
"""

print("[3] A lista elemei: ", end=" ")
print(*dolgozat, sep=", ")

"""
4.	Írassuk ki a lista összegét, átlagát.
"""
osszeg = 0
db = 0
i = 0
for i in dolgozat:
    osszeg = osszeg + i
    db+=1
print(f"[4] Lista összege: {osszeg}\n[4] Átlaga: ~{int(osszeg / db)}")

"""
5.	Írassuk ki a lista páros elemeinek összegét, átlagát, darabszámát.
"""
maxertek = db
osszeg = 0
db = 0
i = 0
while (i < maxertek):
    if (dolgozat[i] % 2 == 0):
        osszeg = osszeg + dolgozat[i]
        db+=1
    i+=1

print(f"[5] Páros elemek összege: {osszeg}\n[5] Átlaguk: ~{int(osszeg / db)}\n[5] Darabszámuk: {db}")

"""
6.	Válogassuk ki egy „parosak” nevű listába a páros elemeket.
"""
parosak = []
i = 0
while (i < maxertek):
    if (dolgozat[i] % 2 == 0):
        parosak.append(dolgozat[i])
    i+=1

"""
7.	Válogassuk szét „kicsi” és „nagy” listába a 40 alatti és a 40 feletti elemeket.
"""
kicsi = []
nagy = []
i = 0

while(i < maxertek):
    if (dolgozat[i] > 40):
        nagy.append(dolgozat[i])
    else:
        kicsi.append(dolgozat[i])
    i+=1

"""
8.	A „negyzetek” listába kerüljenek a „kicsi” lista elemeinek a négyzetei.
"""
negyzetek = []
i = 0
while (i < len(kicsi)):
    negyzetek.append(kicsi[i] ** 2)
    i+=1

"""
9.	Eleme-e a „dolgozat” listának a 42? Ha igen, akkor hányadik eleme?
"""
i = 0
index = 0
talalt = False
while (i < maxertek and talalt == False):
    if (dolgozat[i] == 42):
        index = i
        talalt = True
    i+=1

if (talalt == True):
    print(f"[9] A dolgozat listának eleme a 42. Indexe: {index}")
else:
    print("[9] A dolgozat listának nem eleme a 42.")

"""
10.	Mennyi a „dolgozat” lista páratlan elemei közül a legnagyobb, és a legkisebb?
"""
legkisebb = dolgozat[maxertek - 1]
legnagyobb = dolgozat[0]
i = 0

while (i < maxertek):
    if (dolgozat[i] % 2 != 0 and dolgozat[i] < legkisebb):
        legkisebb = dolgozat[i]
    if (dolgozat[i] % 2 != 0 and dolgozat[i] > legnagyobb):
        legnagyobb = dolgozat[i]
    i+=1

print(f"[10] A dolgozat lista legkisebb páratlan eleme: {legkisebb}\n[10] Legnagyobb páratlan eleme: {legnagyobb}")

#BEZÁRÁS DODGE
input("NYOMJON [ENTER] BILLENTYŰT A BEZÁRÁSHOZ")
