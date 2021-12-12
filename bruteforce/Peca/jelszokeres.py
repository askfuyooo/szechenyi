import pyautogui
import time
a = 1

x = input("Ird be a jelszavad?      ")
jelszo = ""
while a > 0:
    jelszo = input("Mi a jelszo?    ")
    if jelszo == x:
        print("Helyes jelszo")
        a = 0
        break
    else:
        jelszo = input("Mi a jelszo?    ")

time.sleep(120)
