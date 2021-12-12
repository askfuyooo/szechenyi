from random import *
from math import *

# ELSŐ FELADAT
print("%%% ELSŐ FELADAT %%%")
elsoszaz = []
db = 1
while (db <= 100):
    elsoszaz.append(db)
    db+=1
print("Első száz szám összege:", sum(elsoszaz))

# MÁSODIK FELADAT
print("\n%%% MÁSODIK FELADAT %%%")
elsoszazparos = []
db = 1
while (db <= 100):
    if (db % 2 == 0):
        elsoszazparos.append(db)
    db+=1
print("Első száz páros szám összege:", sum(elsoszazparos))

# HARMADIK FELADAT
print("\n%%% HARMADIK FELADAT %%%")
x = int(input("Adjon meg egy számot: "))
db = 1
ertek = 1
while (db <= x):
    ertek = ertek * db
    db+=1
print(x, "faktoriálisa:", ertek)

# NEGYEDIK FELADAT
print("\n%%% NEGYEDIK FELADAT %%%")
x = int(input("Adjon meg egy számot: "))
db = 1
osztok = 0
while (db <= x):
    if (x % db == 0):
        osztok+=1
    db+=1
if (osztok == 2):
    print(x, "prímszám.")
else:
    print(x, "nem prímszám.")

# ÖTÖDIK FELADAT
print("\n%%% ÖTÖDIK FELADAT %%%")
randomok = []
db = 1
while (db <= 10):
    randomok.append(randint(1, 100))
    db+=1
print(randomok)
print("Összege:", sum(randomok), "\nÁtlaga:", int(sum(randomok) / len(randomok)))
print("Legkisebb:", min(randomok), "\nLegnagyobb:", max(randomok))

# BEZÁRÁS DODGE
input("\n\nBEZÁRÁS [ENTER] GOMBBAL!")
