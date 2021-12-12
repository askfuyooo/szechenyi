#TÓTH ÁDÁM | 10. F
"""
1. Feladat:
Hozzunk létre egy üres listát „szamok” néven.
"""
szamok = []


"""
2. Feladat:
Kérjünk be egy Kezdő (K) és egy Vég értéket (V), valamint egy (L) Lépésközt. 
"""
kezdoertek = int(input("Adjon meg egy kezdőértéket: "))
vegertek = int(input("Adjon meg egy végértéket: "))
lepeskozertek = int(input("Adjon meg egy lépésközértéket: "))


"""
3. Feladat:
Írassuk ki a képernyőre a számokat K..V között. 
"""
x = kezdoertek
while x <= vegertek:
    szamok.append(x)
    x+=1
print("[3] Intervallumban lévő számok: ", end="")
print(*szamok, sep=", ")


"""
4. Feladat:
Írassuk ki a képernyőre a számokat K..V között, L lépésközzel.
"""
x = kezdoertek
lepeskozzel = []
while x <= vegertek:
    lepeskozzel.append(x)
    x+=lepeskozertek
print("[4] Számok lépésközzel: ", end="")
print(*lepeskozzel, sep=", ")

"""
5. Feladat:
Írassuk ki a [K..V] intervallumba eső páros számokat.
"""
parosak = []
for x in szamok:
    if x % 2 == 0:
        parosak.append(x)
print("[5] Párosak az intervallumból: ", end="")
print(*parosak, sep=", ")


"""
6. Feladat:
Írassunk ki a [K..V] intervallumba eső 5 darab páros véletlenszámot.
"""
from random import *
randomok = []
x = 1
while x <= 5:
    randomszam = randint(kezdoertek, vegertek)
    if randomszam in parosak:
        randomok.append(randomszam)
        x+=1
print("[6] Random páros számok az intervallumból: ", end="")
print(*randomok, sep=", ")


"""
7. Feladat:
Határozzuk meg az első 8 db [K..V] intervallumba eső véletlenszám összegét,
átlagát, maximumát, minimumát.
"""
elsonyolc = []
x = 0
while x < 8:
    elsonyolc.append(randint(kezdoertek, vegertek))
    x+=1
print("[7] 8db random szám: ", end="")
print(*elsonyolc, sep=", ")
print("Összegük:", sum(elsonyolc), "\nÁtlaguk:", int(sum(elsonyolc) / len(elsonyolc)), "\nMaximuma:", max(elsonyolc), "\nMinimuma:", min(elsonyolc))

#BEZÁRÁS DODGE
input("BEZÁRÁSHOZ NYOMJON [ENTER]-T")
