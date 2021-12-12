from random import *

szamok = []
i = 0

while (i < 10):
    szamok.append(int(random() * 100))
    i+=1

lefut = False

while(lefut == False):
    try:
        x = int(input("Adjon meg egy számot, amely a lista 2. helyére kerül: "))
        lefut = True
    except:
        print("Igazi számot adjon meg!\n")

szamok[1] = x
szamok.sort()

print("A lista növekvő sorrendben: ", end="")
print(*szamok, sep=", ")
