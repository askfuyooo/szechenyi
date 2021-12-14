"""
1. feladat: 
Tölts fel egy 11 elemű listát autómárka nevekkel futási időben (standard inputról).
Feltöltést követően cseréld fel az egyes elemeket úgy, hogy az elsőt az utolsóval,
a másodikat az utolsó előttivel, a harmadikat az (n-3). elemmel, és így tovább.
A középső elemet pedig a sikeres cserék után írd át a "GYŐZELEM" szóra. Írasd ki az új listát a képernyőre.
"""

automarkak = []
i = 0
n = 11

while (i < n):
    lefut = False
    while (lefut == False):
        marka = input(f"[1.F] Adja meg a(z) {i + 1}. autómárkát: ")
        if (marka != ""):
            automarkak.append(marka)
            lefut = True
    i+=1

print("[1.F] A megadott autómárkák: ", end="")
print(*automarkak, sep=", ")

uj_automarkak = []
for i in reversed(automarkak[6:]):
    uj_automarkak.append(i)

uj_automarkak.append("GYŐZELEM")

for i in reversed(automarkak[:5]):
    uj_automarkak.append(i)

print("[1.F] Megadott autómárkák: ", end="")
print(*automarkak, sep=", ")

print("[1.F] Autómárkák rendezve: ", end="")
print(*uj_automarkak, sep=", ")

"""
2. feladat:
Hozz létre egy új listát összefűzéssel (concatenating) az alábbi módon:

Adott a 
bemenet = ['p', 'q'] 
és fűzz az egyes elemeihez (p és q) sorszámokat 1-10-ig.
Tehát n = 10.
Az eredmény lista nézzen ki így:
uj_lista = ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', ... és így tovább p10-ig és q10-ig]
"""

bemenet = ['p', 'q']
uj_lista = []
n = 10
i = 0

while (i < n):
    uj_lista.append(bemenet[0] + str((i + 1)))
    uj_lista.append(bemenet[1] + str((i + 1)))
    i+=1

print("[2.F] Összefűzött lista: ", end="")
print(*uj_lista, sep=", ")

"""
3. feladat:
Adott egy lista:
lista = [1, 2, 3, 4, 5]
Hozz létre belőle egy új listát, úgy, hogy allistákban szerepeljenek az egyes listaelemek hatványai.
Mindegyik elemnek önmaga legyen a legnagyobb hatványa.
pl: 
1**1=1
2**1=2 és 2**2=4
3**1=1 és 3**2=9 és 3**3=27
...és így tovább.
hatvany_lista = [ [1], [2, 4], [3, 9, 27], ...]
A számokat természetesen a hatványozás képletével kell kiszámolni, nem manuálisan beírni.
"""

lista = [1, 2, 3, 4, 5]
hatvany_lista = []
hozzaad_lista = []

for i in range(len(lista)):
    hozzaad_lista = []
    j = 1
    while (j < lista[i] + 1):
        hozzaad_lista.append(lista[i] ** j)
        j+=1
    hatvany_lista.append(hozzaad_lista)

print("[3.F] Hatvány lista: ", end="")
print(*hatvany_lista, sep=", ")

"""
5. feladat:
Adott egy lista:
lista = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
Írj egy programot, amely a nulla digiteket a lista végére pakolja, a többi elemet pedig abban a sorrendben hagyja, ahogy volt.
Az eredmény így kell, hogy kinézzen:
lista = [3, 4, 6, 2, 6, 7, 6, 9, 10, 7, 4, 4, 5, 3, 2, 9, 7, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
"""

lista = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]

print("[4.F] Alap lista: ", end="")
print(*lista, sep=", ")

db = 0
while (lista.count(0) != 0):
    i = 0
    while (i < len(lista)):
        if (lista[i] == 0):
            del(lista[i])
            db+=1
        i+=1

i = 0
while (i < db):
    lista.append(0)
    i+=1

print("[4.F] Szortírozott lista: ", end="")
print(*lista, sep=", ")



#BEZÁRÁS DODGE
input("BEZÁRÁSHOZ NYOMJON [ENTER] BILLENTYŰT!")
