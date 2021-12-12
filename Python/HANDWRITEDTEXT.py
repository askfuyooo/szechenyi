from time import *
from random import *

text = input("Adjon meg egy üzenetet: ")
print()

for msg in text:
    print(msg, end="", flush = True)
    sleep(0.05)

print("\n\n")
endtext = "PRESS [ENTER] TO CLOSE"

for endmsg in endtext:
    print(endmsg, end="", flush = True)
    sleep(0.05)

input("\n")
