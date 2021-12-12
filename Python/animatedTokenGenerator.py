from random import *
from time import *

chars = "ABCDEFGHIKLMNOPQRSTVXYZ0123456789"

def randomGenerator():
    return choice(chars)

token = ""
line = 0


lefut = False
while (lefut == False):
    try:
        charsRange = int(input("Hány karakter legyen összesen? "))
        lefut = True
    except:
        print("\nIgazi számot adjon meg!")

lefut = False
while (lefut == False):
    try:
        charsLine = int(input("Hány karakterenként legyen elválasztva kötőjellel? "))
        lefut = True
    except:
        print("\nIgazi számot adjon meg!")



#TÖRÖLHETŐ, EGYÉNI VÉLEMÉNY: SZERINTEM MENŐ EGY ILYEN SCRIPTHEZ! :D
animation = ""

for i in range(100):
    print(f"Token generálása... {i + 1}%", end="\r")
    sleep(0.01)
print()
#


for i in range(charsRange):
    token = token + str(randomGenerator())
    line+=1
    if (line % charsLine == 0 and i != charsRange - 1):
        token = token + "-"

print(f"Karakterek száma: {charsRange}\nKarakterek egy tömbben (elválasztva): {charsLine}\nToken: \"{token}\"")

#BEZÁRÁS DODGE
input("\n\nBEZÁRÁS [ENTER] GOMBBAL!")
