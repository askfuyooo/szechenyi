"""
Csapadek
Áprilisban (30 napos hónap) minden napon megmértük és feljegyeztük a csapadék mennyiségét mm-ben.
Tároltuk az „eso” nevű listában!
1-én nem esett semmi. 2.-ától, 15.-éig minden nap 8 mm eső hullott.
16.-tól 30.-áig véletlenszámokkal állítsuk elő a csapadékmennyiséget a [0,20] mm intervallumban.

Feladatok:
1.	Lista feltöltése a megadott feltételek szerint.
"""

eso = [0]
i = 0
while (i < 14):
    eso.append(8)
    i+=1

i = 0
from random import randint
while (i < 15):
    eso.append(randint(0, 20))
    i+=1


"""
2.	Legcsapadékosabb nap kiválasztása, dátummal, értékkel.
"""

i = 0
maxindex = 0
maxertek = eso[maxindex]

while (i < len(eso)):
    if (eso[i] > maxertek):
        maxindex = i
        maxertek = eso[i]
    i+=1

print(f"Legcsapadékosabb nap: {maxindex + 1}. értéke: {maxertek}mm")


"""
3.	Hány esőmentes nap volt?
"""

i = 0
db = 0

while (i < len(eso)):
    if (eso[i] == 0):
        db+=1
    i+=1

print(f"{db} nap volt esőmentes.")

"""
4.	Számoljunk átlagot egész hónapra!
"""

ertek = 0
i = 0

while (i < len(eso)):
    ertek = ertek + eso[i]
    i+=1

atlag = ertek / len(eso)
print(f"Egész hónapos átlag: {atlag}mm ~ {int(atlag)}mm")


"""
5.	Számoljuk ki azoknak a napoknak az átlagát, amikor esett eső!
"""
ertek = 0
db = 0
i = 0

while (i < len(eso)):
    if (eso[i] != 0):
        ertek = ertek + eso[i]
        db+=1
    i+=1

atlag = ertek / db

print(f"{db} napon esett az eső, átlaga: {atlag}mm ~ {int(atlag)}mm.")

"""
6.	A felhasználótól bekért napra adjuk meg a csapadék mennyiségét. 
"""
# NAP BEKÉRÉS
lefut = False
while (lefut == False):
    try:
        nap = int(input("Melyik napra állítsunk értéket? "))
        if (nap > 30 or nap < 1):
            print("A hónap 30 napból áll.")
        else:
            lefut = True
    except:
        print("\nIgazi napot adjon meg!")

#MENNYISÉG BEKÉRÉS
lefut = False
while (lefut == False):
    try:
        mennyiseg = int(input(f"A hónap {nap}. napján hány mm csapadék esett? "))
        if (mennyiseg < 0):
            print("Nem eshet minuszban az eső...")
        else:
            lefut = True
    except:
        print("\nIgazi számot adjon meg!")

eso[nap - 1] = mennyiseg

print(f"A hónap {nap}. napjára eső csapadékmennyiség értéke {mennyiseg}mm-re változott!")

"""
7.	Adjuk meg a hónap folyamán leesett összes csapadék mennyiségét. 
"""

ertek = 0
i = 0
while (i < len(eso)):
    ertek = ertek + eso[i]
    i+=1

print(f"A hónap folyamán {ertek}mm eső esett.")


#KILÉPÉS DODGE
input("\n\nKILÉPÉSHEZ NYOMJON [ENTER] BILLENTYŰT!")
