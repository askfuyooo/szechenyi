import os
import pyautogui as pgui
import keyboard as kb
import time

print("Használat:\n[1] Hozz létre az asztalodon egy 'loginlol' nevű mappát!\n[2] A 'loginlol' mappában hozz létre a fiók nevével egy mappát! Pl: 'Felhasznalonevem' (Idézőjelek nélkül)\n[3] Az asztalon lévő 'loginlol\Felhasznalonevem' mappában hozz létre egy 'jelszo.txt' fájlt.\n[4] A 'jelszo.txt' fájl első sorába írd be a fiókhoz tartozó jelszót.\n[5] Kattints a Riot bejelentkező panelénél a felhasználónév szövegdobozra!\n[6] Nyomj 'l' betűt a bejelentkezéshez!")

koz = "    "
desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
felhaszn = input("\n\nFiók neve: ")
print("\nStatus: Fájl létezésének ellenőrzése.")
location = desktop + "\\loginlol\\" + felhaszn + "\jelszo.txt"
ido = time.asctime( time.localtime(time.time()) )

if os.path.isfile(desktop + "\\loginlol\\" + felhaszn + "\jelszo.txt"):
    print("Status: 'jelszo.txt' fájl létezik.")
    file = open(desktop + "\\loginlol\\" + felhaszn + "\jelszo.txt")
    Password = file.readline()
    TPressed = False
    i = 0
    print("\nStatus: Várakozás 'l' gomb lenyomására.")
    while TPressed == False:
        if kb.is_pressed("l"):
            log = " -Sikeres bejelentkezés"
            pgui.press("backspace")
            pgui.press("enter")
            pgui.write(felhaszn)
            time.sleep(0.5)
            pgui.press("enter")
            pgui.press("tab")
            pgui.write(Password)
            time.sleep(0.5)
            while (i < 4):
                pgui.press("tab")
                i+=1
            pgui.press("space")
            pgui.press("tab")
            pgui.press("enter")
            TPressed = True
else:
    print("'jelszo.txt' fájl nem található!\nNyomj [ENTER] gombot bezáráshoz!")
    log = " -Sikertelen bejelentkezés"
    input()
    exit


f = open(desktop + "\\loginlol\\" + "\logs.txt", "a")
ido = time.asctime( time.localtime(time.time()))
szov = ido + log + koz + felhaszn
f.write(szov)
f.write("\n")
f.close()
