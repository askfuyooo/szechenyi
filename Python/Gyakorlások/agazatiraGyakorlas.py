"""
1. generálj 30 random számot! 1-350ig
2. írasd ki az összegét, átlagát a SZAMOK tömbnek!
3. Minimum, Maximum számítása a tömbnek
4. Definiáld a tömböt úgy, hogy növekvő és utána csökkenő sorrendbe írja ki kérés alapján!
5. Melyik számok oszthatók 3-mal, és 5-tel a tömbön belül? Ezeket gyűjtsd ki külön OSZTHATO listába!
6. Írassa ki azokat a számokat amelyek kisebb/egyenlőek 92-nél!
6+1.Írassa ki a prímszámokat és adja hozzá a PRIMSZAM tömbhöz!
"""

#1
from random import randint

SZAMOK = []
for i in range(30):
    SZAMOK.append(randint(1, 350))

#2
osszeg = 0
for i in SZAMOK:
    osszeg += i

atlag = osszeg / len(SZAMOK)

print(f"Összege: {osszeg}\nÁtlaga: {atlag}")

#3
maximum = SZAMOK[0]
i = 0
while (i < len(SZAMOK)):
    if (SZAMOK[i] > maximum):
        maximum = SZAMOK[i]
    i += 1

minimum = SZAMOK[0]
i = 0
while (i < len(SZAMOK)):
    if (SZAMOK[i] < minimum):
        minimum = SZAMOK[i]
    i += 1

print(f"Maximum: {maximum}\nMinimum: {minimum}")

#4
def rendez(lista, valasz):
    if (valasz == "C"):
        lista.sort(reverse=True)
        return lista
    elif (valasz == "N"):
        lista.sort()
        return lista


elfogadva = False
kiirValasz = ""
while (elfogadva == False):
    felhasznaloValasz = input("\"C\"sökkenő vagy \"N\"övekvőbe rendezzem a listát? $").upper()
    if (felhasznaloValasz == "N"):
        elfogadva = True
        kiirValasz = "növekvő"
    elif (felhasznaloValasz == "C"):
        elfogadva = True
        kiirValasz = "csökkenő"
    else:
        print("Válaszoljon \"C\"-vel, ha csökkenőbe, \"N\"-nel, ha növekvőbe szeretnél rendezni a listát.")


SZAMOK = rendez(SZAMOK, felhasznaloValasz)
print(f"A lista {kiirValasz} sorrendben:")
print(*SZAMOK, sep=", ")

#5
OSZTHATO = []
for i in SZAMOK:
    if i % 3 == 0 and i % 5 == 0:
        OSZTHATO.append(i)

print("Osztható 3-mal és 5-tel:")
print(*OSZTHATO, sep=", ")

#6
print("92-nél kisebb/egyenlő:")
for i in SZAMOK:
    if i <= 92:
        print(i, end=", ")
print()

#6+1
PRIMSZAMOK = []
for i in SZAMOK:
    osztoi = 0
    for j in range(1, i+1):
        if (i % j == 0):
            osztoi += 1
    if (osztoi == 2):
        PRIMSZAMOK.append(i)


print("Prímszámok:")
print(*PRIMSZAMOK, sep=", ")
