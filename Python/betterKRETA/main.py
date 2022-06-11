class projectBeallitasok:
    def __init__(self, nev, verzio) -> None:
        self.nev = nev
        self.verzio = verzio

pB = projectBeallitasok("betterKRÉTA", "0.1")

import os
import time
import shutil

os.system(f"title {pB.nev}")
currentDirectory = os.getcwd() + "/"
os.system("cls")
print(f"{pB.nev} | Ver. {pB.verzio}\n")


class beallitasok:

    def kilepes():
        input("Kilépéshez nyomjon [ENTER] billentyűt!")
        time.sleep(0.25)
        exit()

    class ellenorzes:
        def vanEOsztaly():
            if (os.path.exists(currentDirectory + "osztalyok")):
                return True
            else:
                return False
    
    class osztaly:
        def __init__(self, nev) -> None:
            self.nev = nev

    class szerkesztes:
        def osztaly():
            if (beallitasok.ellenorzes.vanEOsztaly()):
                osztalyok = []
                for osztaly in os.listdir("osztalyok"):
                    osztalyok.append(osztaly)

                print(f"Szerkeszthető osztályok száma: {len(osztalyok)}")
                if (len(osztalyok) == 0):
                    print("Úgy látszik, még egy osztály sincs létrehozva.\nÁtirányítjuk az osztálylétrehozó menüre.")
                    print("Átirányítás 5mp múlva...")
                    time.sleep(5)
                    beallitasok.letrehoz.osztaly()
                
                print("Szerkeszthető osztályok:")
                print(*osztalyok, sep="\n")
                
                elfogadva = False
                while (elfogadva == False):
                    szerkesztendo = input("Melyik osztályt szeretné szerkeszteni? $")
                    if szerkesztendo in osztalyok:
                        allitandoOsztaly = beallitasok.osztaly(szerkesztendo)
                        editClass = szerkesztendo
                        elfogadva = True
                    elif szerkesztendo.upper() == "EXITC":
                        beallitasok.mutat.menu()
                    else:
                        print("Az osztály nem létezik! Ellenőrízze, hogy helyesen írta-e be. Kilépéshez írja be: \"EXITC\"")

                os.system("cls")
                print(f"== {pB.nev} osztályszerkesztő ==")
                print(f"== {allitandoOsztaly.nev} szerkesztése ==")
                
                print("[0] vissza a menübe")
                print("[1] tanuló hozzáadása")



                elfogadva = False
                while (elfogadva == False):
                    try:
                        valasz = int(input("Adja meg a választott opciót! $"))
                        if (valasz == 0):
                            elfogadva = True
                            beallitasok.mutat.menu()
                        elif (valasz == 1):
                            elfogadva = True


                            os.system("cls")
                            print(f"== {allitandoOsztaly.nev} | tanuló hozzáadása ==")
                            jelenlegiTanulok = [] #jelenlegi tanulók mentése
                            with open("osztalyok/" + allitandoOsztaly.nev + "/diakok", "r", encoding="utf8()") as f:
                                for sor in f.readlines():
                                    splitelve = sor.split("\n")
                                    jelenlegiTanulok.append(splitelve[0])

                            tanuloID = 0
                            try:
                                utolsoTanulo = jelenlegiTanulok[-1].split(";")
                                tanuloID = int(utolsoTanulo[0]) + 1
                            except:
                                pass

                            hozzadasVege = False
                            tanuloAdatok = []
                            #tanuloID = id
                            #0 - vezeteknev
                            #1 - keresztnev
                            #2 - szul. datuom
                            #3 - nem
                            #4 - lakhely
                            #5 - email cim
                            #6 - telefonszam
                            #7 - apja neve
                            #8 - anyja neve
                            while (hozzadasVege == False):
                                tanuloAdatok = []
                                tanuloAdatok.append(input("Adja meg a tanuló vezetéknevét: $"))
                                tanuloAdatok.append(input("Adja meg a tanuló keresztnevét: $"))
                                tanuloAdatok.append(input("Adja meg a tanuló születési dátumát a következő formában: \"YYYY/MM/DD\" $"))
                                tanuloAdatok.append(input("Adja meg a tanuló nemét: $"))
                                tanuloAdatok.append(input("Adja meg a tanuló lakhelyét: $"))
                                tanuloAdatok.append(input("Adja meg a tanuló email címét: $"))
                                tanuloAdatok.append(input("Adja meg a tanuló telefonszámát: $"))
                                tanuloAdatok.append(input("Adja meg a tanuló apjának nevét: $"))
                                tanuloAdatok.append(input("Adja meg a tanuló anyjának nevét: $"))

                                os.system("cls")
                                print(f"== {allitandoOsztaly.nev} | adatok ellenőrzése ==")


                                print(f"Tanuló vezetékneve: {tanuloAdatok[0]}")
                                print(f"Tanuló keresztneve: {tanuloAdatok[1]}")
                                print(f"Tanuló születési dátuma: {tanuloAdatok[2]}")
                                print(f"Tanuló neme: {tanuloAdatok[3]}")
                                print(f"Tanuló lakhelye: {tanuloAdatok[4]}")
                                print(f"Tanuló email címe: {tanuloAdatok[5]}")
                                print(f"Tanuló telefonszáma: {tanuloAdatok[6]}")
                                print(f"Tanuló apjának neve: {tanuloAdatok[7]}")
                                print(f"Tanuló anyjának neve: {tanuloAdatok[8]}\n")

                                megerositve = False
                                while (megerositve == False):
                                    valasz = input("Helyesek az adatok? [y/n] $").upper()

                                    if (valasz == "Y"):
                                        hozzadasVege = True
                                        megerositve = True
                                    elif (valasz == "N"):
                                        print("Ebben az esetben újra kell kezdeni a létrehozást!")
                                        megerositve = True
                                    else:
                                        print("Kérem válszoljon igennel [y] vagy nemmel [n]!")


                            ujTanulo = f"{tanuloID};{tanuloAdatok[0]};{tanuloAdatok[1]};{tanuloAdatok[2]};{tanuloAdatok[3]};{tanuloAdatok[4]};{tanuloAdatok[5]};{tanuloAdatok[6]};{tanuloAdatok[7]};{tanuloAdatok[8]};"
                            
                            jelenlegiTanulok.append(ujTanulo)

                            print("Tanuló mentése...")
                            with open("osztalyok/" + allitandoOsztaly.nev + "/diakok", "w", encoding="utf8()") as f:
                                for tanulo in jelenlegiTanulok:
                                    f.writelines(tanulo + "\n")
                            print("Tanuló mentve.")

                            print("Átirányítás 3mp múlva...")
                            time.sleep(3)
                            beallitasok.mutat.menu()

                        else:
                            print("Nem létező opció!")
                    except:
                        print("Valódi számot adjon meg!")

            else:
                print("Nem szerkeszthetsz osztályokat, amég nem léteznek!")
                print("Átirányítás az osztálylétrehozó menüre 3mp múlva...")
                time.sleep(3)
                beallitasok.letrehoz.osztaly()

    class mutat:
        def menu():
            os.system("cls")
            print(f"== {pB.nev} v{pB.verzio} ==")
            print("Üdvözöljük a menüben!")
            print("[0] menü újratöltése")
            print("[1] osztály létrehozása")
            print("[2] osztály szerkesztése")
            print("[99] RESET")
            print("[100] kilépés")

            elfogadva = False
            while (elfogadva == False):
                try:
                    valasz = int(input("Adja meg a választott opciót! $"))
                    if (valasz == 0):
                        elfogadva = True
                        beallitasok.mutat.menu()
                    elif (valasz == 1):
                        elfogadva = True
                        beallitasok.letrehoz.osztaly()

                    elif (valasz == 2):
                        elfogadva = True
                        beallitasok.szerkesztes.osztaly()

                    elif (valasz == 99):
                        megerositve = False
                        while (megerositve == False):
                            megValasz = input("A RESET folyamat végleges, és nem visszafordítható!!!\nEnnek ellenére RESET-eli a programot? [y/n] $").upper()
                            if (megValasz == "Y"):
                                print("RESET kezdése...")
                                try:
                                    shutil.rmtree("osztalyok")
                                    print("RESET sikeres.")
                                    megerositve = True
                                    elfogadva = True
                                    beallitasok.mutat.menu()
                                except:
                                    print(f"RESET sikertelen. Hiba: Valószínűleg már RESET-elve van a program.")
                                    megerositve = True
                            elif (megValasz == "N"):
                                megerositve = True
                            else:
                                print("Kérem válszoljon igennel [y] vagy nemmel [n]!")

                    elif (valasz == 100):
                        elfogadva = True
                        beallitasok.kilepes()

                    else:
                        print("Nem létező opció!")
                except:
                    print("Valódi számot adjon meg!")

        def elsoInditas():
            elfogadva = False
            while (elfogadva == False):
                valasz = input("Úgy látszik, nincsenek még osztályok létrehozva.\nKíván létrehozni egyet? [y/n] $").upper()
                if (valasz == "Y"):
                    elfogadva = True
                    beallitasok.letrehoz.osztaly()

                elif (valasz == "N"):
                    elfogadva = True
                    beallitasok.mutat.menu()
                else:
                    print("Kérem válaszoljon igennel [y] vagy nemmel [n]!")
                

    class letrehoz:
        def osztaly():
            os.system("cls")
            print(f"== Üdvözöljük a(z) {pB.nev} osztálylétrehozó panelénél! ==")
            elfogadva = False
            while (elfogadva == False):
                letrehozandoOsztaly = input("Kérem adja meg a létrehozandó osztály nevét! $")
                valasz = input(f"Megerősíti a(z) \"{letrehozandoOsztaly}\" osztály létrehozását? [y/n] Kilépéshez írja be: \"EXITC\"! $").upper()
                if (valasz == "Y"):
                    elfogadva = True
                elif (valasz == "EXITC"):
                    beallitasok.mutat.menu()
                elif (valasz == "N"):
                    print("Megerősítés megszakítva.")
                else:
                    print("Kérem válszoljon igennel [y] vagy nemmel [n]! Kilépéshez válaszoljon \"EXITC\"-val/vel!")
            
            print("Osztályok mappa keresése...")
            if (beallitasok.ellenorzes.vanEOsztaly()):
                print("Mappa létezik.")
            else:
                print("Mappa nem létezik.\nMappa létrehozása...")
                os.mkdir("osztalyok")
                print("Mappa létrehozva!")
            
            print("Létrehozandó osztály ellenőrzése...")
            if (os.path.exists("osztalyok/" + letrehozandoOsztaly)):
                print(f"\"{letrehozandoOsztaly}\" osztály már létezik, így nem lesz lérehozva!")
                print("Átirányítás 5mp múlva...")
                time.sleep(5)
                beallitasok.mutat.menu()
            else:
                print("Osztály mappa létrehozása...")
                defaultPath = "osztalyok/" + letrehozandoOsztaly
                os.mkdir(defaultPath)
                defaultPath += "/"
                with open(defaultPath + "diakok", "w", encoding="utf8()") as f:
                    f.write("")
                with open(defaultPath + "jegyek", "w", encoding="utf8()") as f:
                    f.write("")
                with open(defaultPath + "tantargyak", "w", encoding="utf8()") as f:
                    f.write("")
                print(f"\"{letrehozandoOsztaly}\" osztály sikeresen létrehozva!")
                print("Átirányítás 5mp múlva...")
                time.sleep(5)
                beallitasok.mutat.menu()
            


#main start
print("Osztályok keresése...")
if (beallitasok.ellenorzes.vanEOsztaly()):
    beallitasok.mutat.menu()
else:
    beallitasok.mutat.elsoInditas()
