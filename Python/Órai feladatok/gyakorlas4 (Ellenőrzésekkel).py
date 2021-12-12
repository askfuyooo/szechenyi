"""
Kérjünk be három egész számot, és határozzuk meg, hogy számtani sorozatot alkotnak-e.
(szomszédos elemek különbsége egyenlő, pl: 3, 5, 7).
Ha igen, adjuk meg a szomszédos elemek különbségét. Pl: d=2. 
Vizsgáljuk meg, hogy mértani sorozatot alkotnak-e
(szomszédos elemek hányadosa állandó, pl: 2, 4, 8).
Ha igen, adjuk meg a szomszédos elemek hányadosát. Pl: q=2.
"""
szamtani = False
mertani = False
d = 0
q = 0

lefut = False
while (lefut == False):
    try:
        x = int(input("Adja meg az első számot: "))
        lefut = True
    except:
        print("Igazi számot adjon meg!\n")
        
lefut = False
while (lefut == False):
    try:
        y = int(input("Adja meg az második számot: "))
        lefut = True
    except:
        print("Igazi számot adjon meg!\n")

lefut = False
while (lefut == False):
    try:
        z = int(input("Adja meg az harmadik számot: "))
        lefut = True
    except:
        print("Igazi számot adjon meg!\n")


d = x - y
if (d == y - z):
    szamtani = True

q = y / x
if (y * q == z):
    mertani = True



if (d <= 0):
    d = d*-1
q = int(q)



if (szamtani == True and mertani == True):
    print(x, y, z, "számtani és mértani sorozat is. d=", d, "q=", q)
elif (szamtani == True and mertani == False):
    print(x, y, z, "számtani sorozat. d=", d)
elif (szamtani == False and mertani == True):
    print(x, y, z, "mértani sorozat. q=", q)
elif (szamtani == False and mertani == False):
    print(x, y, z, "se számtani, se mértani sorozat.")
else:
    print("Hiba.")
