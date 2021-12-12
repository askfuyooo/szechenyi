"""
100 elemű lista, 0-1000-ig random számok. Első fele növekvő, második fele csökkendő 
"""
from random import *

lista = []

i = 0
while (i < 100):
    lista.append(randint(0, 1000))
    i+=1

i = 0
elsofele = []
masodikfele = []
while (i < len(lista)):
    if (i < 50):
        elsofele.append(lista[i])
    else:
        masodikfele.append(lista[i])
    i+=1

elsofele.sort()
masodikfele.sort(reverse=True)

print("A lista random számokkal: ", end="")
print(*lista, sep=", ")

print("\nA lista első fele növekvő sorrendben: ", end="")
print(*elsofele, sep=", ")

print("\n A lista második fele csökkenő sorrendben: ", end="")
print(*masodikfele, sep=", ")
