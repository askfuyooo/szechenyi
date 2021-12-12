#SZÜKSÉGES IMPORTOK!!: pyautogui, keyboard
#pip install pyautogui
#pip install keyboard

import os
import pyautogui as pag
import keyboard as kb
import time

print("Használat:\n[1] Hozz létre az asztalodon egy 'Logins' nevű mappát!\n[2] A 'Logins' mappában hozz létre a fiók nevével egy mappát! Pl: 'Felhasznalonevem' (Idézőjelek nélkül)\n[3] Az asztalon lévő 'Logins\Felhasznalonevem' mappában hozz létre egy 'creds.txt' fájlt.\n[4] A 'creds.txt' fájl első sorába írd be a fiókhoz tartozó jelszót.\n[5] Kattints a Riot bejelentkező panelénél a felhasználónév szövegdobozra!\n[6] Nyomj 'T' betűt a bejelentkezéshez!")
desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
CurrUser = input("\n\nFiók neve: ")
print("\nStatus: Fájl létezésének ellenőrzése.")
location = desktop + "\\Logins\\" + CurrUser + "\creds.txt"
if os.path.isfile(desktop + "\\Logins\\" + CurrUser + "\creds.txt"):
    print("Status: 'creds.txt' fájl létezik.")
    file = open(desktop + "\\Logins\\" + CurrUser + "\creds.txt")
    Password = file.readline()
    TPressed = False
    i = 0
    print("\nStatus: Várakozás 'T' gomb lenyomására.")
    while TPressed == False:
        if kb.is_pressed('T'):
            pag.press('BACKSPACE')
            pag.write(CurrUser)
            pag.press('ENTER')
            pag.press('TAB')
            pag.write(Password)
            while (i < 4):
                pag.press('TAB')
                i+=1
            pag.press('SPACE')
            pag.press('TAB')
            pag.press('ENTER')
            TPressed = True
else:
    print("'creds.txt' fájl nem található!\nNyomj [ENTER] gombot bezáráshoz!")
    input()
    exit
