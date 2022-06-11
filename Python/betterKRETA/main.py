class projectBeallitasok:
    def __init__(self, nev = "betterKRÉTA", verzio = "0.1") -> None:
        self.nev = "betterKRÉTA"
        self.verzio = "0.1"

pB = projectBeallitasok()

import os
import time
import shutil

os.system(f"title {pB.nev}")
currentDirectory = os.getcwd() + "/"
print(f"{pB.nev} | Ver. {pB.verzio}\n")

class beallitasok:

    def kilepes():
        input("Kilépéshez nyomjon [ENTER] billentyűt!")
        exit()

    class ellenorzes:
        def vanEOsztaly():
            if (os.path.exists(currentDirectory + "osztalyok")):
                return True
            else:
                return False
    
    class szerkesztes:
        def osztaly():
            if (beallitasok.ellenorzes.vanEOsztaly()):
                elfogadva = False
                while (elfogadva == False):
                    pass

                    # IDE JÖHET A SZERKESZTENDŐ OSZTÁLY NEVE, OSZTÁLY LISTÁK, MENÜBE VISSZAUGRÁS


            else:
                print("Nem szerkeszthetsz osztályokat, amég nem léteznek!")
                print("Átirányítás a menüre 5mp múlva...")
                time.sleep(5)
                beallitasok.mutat.menu()

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
                                except:
                                    print(f"RESET sikertelen.")
                                    megerositve = True
                            elif (megValasz == "N"):
                                megerositve = True
                            else:
                                print("Kérem válszoljon igennel [y] vagy nemmel [n]!")

                    elif (valasz == 100):
                        beallitasok.kilepes()

                    else:
                        print("Nem létező opció!")
                except:
                    print("Valódi számot adjon meg!")
                

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
            else:
                print("Osztály mappa létrehozása...")
                defaultPath = "osztalyok/" + letrehozandoOsztaly
                os.mkdir(defaultPath)
                defaultPath += "/"
                with open(defaultPath + "diakok", "w") as f:
                    f.write("")
                with open(defaultPath + "jegyek", "w") as f:
                    f.write("")
                with open(defaultPath + "tantargyak", "w") as f:
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
    elfogadva = False
    while (elfogadva == False):
        valasz = input("Úgy látszik, nincsenek még osztályok létrehozva.\nKíván létrehozni egyet? [y/n] $").upper()
        if (valasz == "Y"):
            elfogadva = True
            beallitasok.letrehoz.osztaly()

        elif (valasz == "N"):
            beallitasok.mutat.menu()
        else:
            print("Kérem válaszoljon igennel [y] vagy nemmel [n]!")
        
