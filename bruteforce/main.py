import pyautogui
import time
import os
import random
import string
x = 1
szam = "0123456789"

szam_list = list(szam)
time.sleep(2)

while x > 0:
    ra = [str(random.randint(0, 9)), str(random.randint(0, 9)), str(random.randint(0, 9)), str(random.randint(0, 9))] #= 4szamjegyu szam
    # str(random.randint(0, 9)) = +1 szam 
    pyautogui.write(ra)
    pyautogui.press("enter") #leggyorsabb szamkereses
