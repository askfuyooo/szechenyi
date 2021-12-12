from random import *
from math import *

#ELSŐ FELADAT
print("%%% ELSŐ FELADAT %%%")
x = int(input("Adja meg az első számot: "))
y = int(input("Adja meg a második számot: "))
if (x<y):
    print("A megadott két szám:", x, "és", y, "a nagyobb:", y)
elif (y<x):
    print("A megadott két szám:", x, "és", y, "a nagyobb:", x)
else:
    print("A megadott két szám:", x, "és", y, "amelyek egyenlőek.")


#MÁSODIK FELADAT
print("\n%%% MÁSODIK FELADAT %%%")
x = int(input("Adja meg az első számot: "))
y = int(input("Adja meg a második számot: "))
z = int(input("Adja meg a harmadik számot: "))
if (x<y and x<z):
    print("A megadott három szám:", x, "és", y, "illetve", z, "a legkisebb:", x)
elif(y<x and y<z):
    print("A megadott három szám:", x, "és", y, "illetve", z, "a legkisebb:", y)
elif(z<x and z<y):
    print("A megadott három szám:", x, "és", y, "illetve", z, "a legkisebb:", z)
elif(x==y and x<z):
    print("A megadott három szám:", x, "és", y, "illetve", z, "a legkisebb:", x)
elif(x==z and x<y):
    print("A megadott három szám:", x, "és", y, "illetve", z, "a legkisebb:", x)
elif(y==z and y<x):
    print("A megadott három szám:", x, "és", y, "illetve", z, "a legkisebb:", y)
else:
    print("Mindhárom egyenlő.", x)


#HARMADIK FELADAT
print("\n%%% HARMADIK FELADAT %%%")
a = int(input("Adja meg a háromszög 'a' oldalát: "))
b = int(input("Adja meg a háromszög 'b' oldalát: "))
c = int(input("Adja meg a háromszög 'c' oldalát: "))
if (a + b > c and a + c > b and b + c > a):
    print("A háromszög oldalai:\na:", a, "\nb:", b, "\nc:", c, "\nA háromszög szerkeszthető.")
else:
    print("A háromszög oldalai:\na:", a, "\nb:", b, "\nc:", c, "\nA háromszög nem szerkeszthető.")


#NEGYEDIK FELADAT
print("\n%%% NEGYEDIK FELADAT %%%")
szam = int(input("Adjon meg pozitív egész számot: "))
szamosztoi = []
i = 1
while (i < szam + 1):
    if (szam % i == 0):
        print(i, end=", ")
        szamosztoi.append(i)
    i+=1
print()
print(szamosztoi)
print(szam, "osztóinak darabszáma:", len(szamosztoi), "\nOsztók összege:", sum(szamosztoi))


#ÖTÖDIK FELADAT
print("\n%%% ÖTÖDIK FELADAT %%%")
i = 0
randomok = []
while (i < 5):
    x = randint(1, 90)
    print("[", i + 1, "]", x)
    randomok.append(x)
    i+=1

print(randomok)
print("A legkisebb:", min(randomok))
print("A legnagyobb:", max(randomok))
print("Összegük:", sum(randomok))


#Bezárás dodge
input("\n\n[BEZÁRÁSHOZ NYOMJON 'ENTER'-T]")
