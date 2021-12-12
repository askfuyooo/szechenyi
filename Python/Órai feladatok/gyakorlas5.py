"""
Kérjük be egy téglalap 'a' és 'b' oldalhosszúságát.
Ellenőrizzük az adatokat, ha negatív, vagy nulla, akkor kérjük be újra.
Írassuk ki a terület és kerület képletét, és értékét is. 
"""

print("1. Feladat\n======")

#"a" bekérése
lefut = False
while (lefut == False):
    try:
        ervenyes = False
        while (ervenyes == False):
            a = int(input("Adja meg a téglalap \"a\" oldalának hosszát: "))
            if (a > 0):
                ervenyes = True
                lefut = True
            else:
                print("\"a\" szám nem lehet kisebb vagy egyenlő nullával!")
    except:
        print("\nIgazi számot adjon meg!")

#"b" bekérése
lefut = False
while (lefut == False):
    try:
        ervenyes = False
        while (ervenyes == False):
            b = int(input("Adja meg a téglalap \"b\" oldalának hosszát: "))
            if (b > 0):
                ervenyes = True
                lefut = True
            else:
                print("\"a\" szám nem lehet kisebb vagy egyenlő nullával!")
    except:
        print("\nIgazi számot adjon meg!")

kerulet = int(2 * (a + b))
terulet = int(a * b)

print(f"Téglalap értékei:\na = {a}cm\nb = {b}cm\nKerület: 2 * (a + b) = 2 * ({a} + {b}) = {kerulet}cm\nTerület: a * b = {a} * {b} = {terulet}cm2\n======")

"""
A felhasználó választhat a következő síkidomok közül:
Háromszög, négyzet, téglalap, kör.
Kérjük be a síkidomnak megfelelő adatokat,
számoljuk ki a választott síkidom kerületét és területét.
Írassuk ki a megadott adatokat, képleteket, és eredményeket is.
"""

print("2. Feladat")
sikidomok = ["háromszög", "négyzet", "téglalap", "kör"]
lefut = False
while (lefut == False):
    print("Válasszon egy síkidomot: ", end="")
    print(*sikidomok, sep=", ")
    valasz = input("Választott síkidom: ")
    if (valasz in sikidomok):
        lefut = True
    else:
        print("A síkidom nem létezik!")

if (valasz == sikidomok[0]): #HÁROMSZÖG
    #"a" bekérése
    lefut = False
    while (lefut == False):
        try:
            a = int(input("Adja meg a háromszög \"a\" oldalának hosszát: "))
            lefut = True
        except:
            print("\nIgazi számot adjon meg!")

    #"b" bekérése
    lefut = False
    while (lefut == False):
        try:
            b = int(input("Adja meg a háromszög \"b\" oldalának hosszát: "))
            lefut = True
        except:
            print("\nIgazi számot adjon meg!")

    #"c" bekérése
    lefut = False
    while (lefut == False):
        try:
            c = int(input("Adja meg a háromszög \"c\" oldalának hosszát: "))
            lefut = True
        except:
            print("\nIgazi számot adjon meg!")
    #"magasság"

    lefut = False
    while(lefut == False):
        ertek = input("Melyik oldalhoz tartozik a magasság? (a, b, c): ")
        if (ertek == "a"):
            ertek = a
            lefut = True
        elif (ertek == "b"):
            ertek = b
            lefut = True
        elif (ertek == "c"):
            ertek = c
            lefut = True
        else:
            print("Hibás/nem létező oldal!")

    #"magasság" bekérése
    lefut = False
    while (lefut == False):
        try:
            magassag = int(input("Adja meg a háromszög \"magasságának\" hosszát: "))
            lefut = True
        except:
            print("\nIgazi számot adjon meg!")

    kerulet = int(a + b + c)
    terulet = int((ertek * magassag) / 2)

    print(f"==={valasz}===\na = {a}cm\nb = {b}cm\nc = {c}cm\nKerület: a + b + c = {a} + {b} + {c} = {kerulet}cm\nTerület: (x * magassagx) / 2 = ({ertek} * {magassag}) / 2 = {terulet}cm2\n==={valasz}===")

elif (valasz == sikidomok[1]): #NÉGYZET
    #"a" bekérése
    lefut = False
    while (lefut == False):
        try:
            a = int(input("Adja meg a négyzet \"a\" oldalának hosszát: "))
            lefut = True
        except:
            print("\nIgazi számot adjon meg!")

    kerulet = int(4 * a)
    terulet = int(a * a)

    print(f"==={valasz}===\na = {a}cm\nKerület: 4 * a = 4 * {a} = {kerulet}cm\nTerület: a * a = {a} * {a} = {terulet}cm2\n==={valasz}===")

elif (valasz == sikidomok[2]): #TÉGLALAP
    #"a" bekérése
    lefut = False
    while (lefut == False):
        try:
            a = int(input("Adja meg a téglalap \"a\" oldalának hosszát: "))
            lefut = True
        except:
            print("\nIgazi számot adjon meg!")

    #"b" bekérése
    lefut = False
    while (lefut == False):
        try:
            b = int(input("Adja meg a téglalap \"b\" oldalának hosszát: "))
            lefut = True
        except:
            print("\nIgazi számot adjon meg!")
    
    kerulet = int(2 * (a + b))
    terulet = a * b

    print(f"==={valasz}===\na = {a}cm\nb = {b}\nKerület: 2 * (a + n) = 2 * ({a} + {b}) = {kerulet}cm\nTerület: a * b = {a} * {b} = {terulet}cm2\n==={valasz}===")

else: #KÖR
    pi = 3.14
    #"r" bekérése
    lefut = False
    while (lefut == False):
        try:
            r = int(input("Adja meg a kör \"r\" hosszát: "))
            lefut = True
        except:
            print("\nIgazi számot adjon meg!")
    
    kerulet = int(pi * (r*r))
    terulet = int(2 * pi * r)

    print(f"==={valasz}===\npi = {pi}\nr = {r}\nKerület: pi * r2 = {pi} * {r*r} = {kerulet}cm\nTerület: 2 * pi * r = 2 * {pi} * {r} = {terulet}cm2\n==={valasz}===")


#BEZÁRÁS DODGE
input("\n\nNYOMJON [ENTER] GOMBOT A BEZÁRÁSHOZ!")
