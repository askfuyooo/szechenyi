from random import *
szamok = []
db = 0
while db <= 100:
    szamok.append(int(random() * 100))
    db+=1
parosak = []
for x in szamok:
    if x % 2 == 0:
        parosak.append(x)

print(*parosak, sep=", ")
print("Párosak száma:", len(parosak))
