"""
!!!
A SCRIPT KIZÁRÓLAG GYAKORLÁS CÉLJÁBÓL KÉSZÜLT!
HASZNÁLATA KIZÁRÓLAG PRACTICE MÓDBAN AJÁNLOTT!
CSALÁSRA ALKALMAZNI TILOS!
A SCRIPT NÉMI BHOP TUDÁST IGÉNYEL!
!!!
SZÜKSÉGES IMPORTOK:
-pip install pyautogui
-pip install keyboard
"""

import os
import time
import keyboard
import pyautogui as pag
bhenabled = False
pag.FAILSAFE = False
def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def printStatus(status):
    if status == True:
        return False
    else:
        return True

def WriteStats(status):
    clear()
    print("%%%%%%%%%%%%%%%%%%")
    print("BHOP STATUS:", status)
    print("%%%%%%%%%%%%%%%%%%")



WriteStats(bhenabled)


while True:
    if keyboard.is_pressed('SPACE'):
        if printStatus(bhenabled) != True:
            pag.press('SPACE')
            #time.sleep(0.015) #EGYÉNI
    if keyboard.is_pressed('M'):
        bhenabled = not bhenabled
        WriteStats(bhenabled)
        time.sleep(1)

#NEM KELL DE MÉGIS
input("BEZÁRÁS [ENTER]")
