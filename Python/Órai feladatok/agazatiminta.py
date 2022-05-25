print("1. Feladat")
"""
1.	feladat:
Írj programot, mely bekér egy kétjegyű egész számot, majd kiszámolja és kiírja annak osztóit!
Csak kétjegyű szám megadásakor fusson a program!
Az osztókat elég csak a szám feléig vizsgálni (szam//2)!
Az osztók egy sorban, pontosvesszővel elválasztva jelenjenek meg!
Ha nem talál osztót írja ki, hogy prímszám!
A program várt működése pl. a következő:
Adj meg egy kétjegyű egész számot: 15
15 osztói:
1; 3; 5; 15
Vagy:
Adj meg egy kétjegyű egész számot: 11
A 11 prímszám.
"""

elfogadva = False
while (elfogadva == False):
    try:
        szam = int(input("Adjon meg egy kétjegyű egész számot: $"))
        if (szam > 9 and szam < 100):
            print(f"Szám {szam} mentve.")
            elfogadva = True
        else:
            print("A számnak kétjegyűnek kell lennie.")
    except:
        print("Valódi számot adjon meg!")

osztok = []
i = 1
while (i <= szam): #Ha elég a szám felét nézni, akkor while (i <= szam / 2), de akkor a prím ellenőrzés is más.
    if (szam % i == 0):
        osztok.append(i)
    i += 1

if (len(osztok) != 2):
    print(f"\n{szam} osztói: ")
    print(*osztok, sep="; ")
else:
    print(f"{szam} prímszám.")



print("\n\n2. Feladat")
"""
2.  feladat:
Állíts elő 10 tagú, 1 és 100 közötti véletlen egész számokból álló listát!
Írj egy saját rendez() nevű függvényt, ami a létrehozott listát a választott módon rendezi!
Kérd be, hogyan legyen rendezve a lista, „Csökkenő” (C) vagy „Növekvő” (N) sorrendbe!
A választás bekérésénél nagybetűt használj! 
A saját függvényed segítségével rendezd a listát a megadott sorrendbe!
Írasd ki a rendezett listát! 
A program várt működése pl. a következő:
'C'sökkenő vagy 'N'övekvő sorrendbe rendezzem a listát? c
[94, 94, 84, 82, 81, 78, 61, 35, 35, 21]
Vagy:
'C'sökkenő vagy 'N'övekvő sorrendbe rendezzem a listát? n
[1, 4, 6, 10, 35, 45, 74, 90, 91, 91]
"""

randomlista = []
from random import randint

for i in range(10):
    randomlista.append(randint(1, 100))

def rendez(lista, valasztas):
    if (valasztas == "C"):
        lista.sort(reverse=True)
        print("A random generált lista csökkenő sorrendben:")
        print(*lista, sep=", ")
    else:
        lista.sort()
        print("A random generált lista növekvő sorrendben:")
        print(*lista, sep=", ")

print("A generált lista:")
print(*randomlista, sep=", ")

elfogadva = False
while (elfogadva == False):
    valasz = input("'C'sökkenő vagy 'N'övekvő sorrendbe rendezzem a listát? $")
    if (valasz == "C" or valasz == "N"):
        elfogadva = True
    else:
        print("A választás csak 'C' vagy 'N' lehet.")

if (valasz == "C"):
    print("A lista csökkenő sorrendben:")
else:
    print("A lista növekvő sorrendben:")

rendez(randomlista, valasz)

input("\n\nA program lefutott.\nBezáráshoz nyomjon [ENTER] billentyűt.")
