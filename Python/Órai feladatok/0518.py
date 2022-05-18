from random import randint

szamok = []

#feltöltés
for i in range(20):
    szamok.append(randint(10, 99))

print(*szamok, sep=", ")

#összeg
osszeg = 0
i = 0
while (i < len(szamok)):
    osszeg += szamok[i]
    i += 1

print(f"Összeg: {osszeg}")

#átlag
atlag = osszeg / len(szamok)

print(f"Átlag: {atlag}")

#min
minimum = szamok[0]
for i in szamok:
    if (i < minimum):
        minimum = i

print(f"Minimum szám: {minimum}")

#max
maximum = szamok[0]
i = 0
while (i < len(szamok)):
    if (szamok[i] > maximum):
        maximum = szamok[i]
    i += 1

print(f"Maximum szám: {maximum}")

#páros
parosdb = 0
for i in szamok:
    if (i % 2 == 0):
        parosdb += 1

print(f"Páros számok száma: {parosdb}")

#50nél kisebb
kisebb = 0
i = 0
while (i < len(szamok)):
    if (szamok[i] < 50):
        kisebb += 1
    i += 1

print(f"50-nél kisebb számok száma: {kisebb}")


#bezárás dodge
input("\nKilépéshez nyomjon [ENTER] billentyűt!")
