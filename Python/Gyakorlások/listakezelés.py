"""
1. Hozz létre egy listát, ami 6 keresztnevet tartalmaz.
"""
keresztnevek = ["Nigger", "Ubul", "Aladár", "Vendel", "Elemér", "Ágoston"]
"""
2. Kérdezd meg a felhasználót, hogy hogy hívják, és a végéhez add hozzá az ő nevét is.
"""
keresztnevek.append(input("Hogy hívnak?: "))
"""
3. Írasd ki, hogy az egyes nevek milyen hosszúak az alábbiak szerint:
    Bence: 5 karakter
"""
for x in keresztnevek:
    print(x, len(x), "karakter")

"""
4. Írasd ki egymás mellé vesszővel elválasztva az összes "A" betűvel kezdődő nevet. (Legyen ilyen a listában.) A nevek is tömbök, a karakterek indexelhetők!
"""
avalkezdodik = []
for x in keresztnevek:
    if (x[0] == "A"):
        avalkezdodik.append(x)
print("A-val kezdődő nevek: ", end="")
print(*avalkezdodik, sep=", ")
"""
5. Döntsd el, hogy a mindenkori utolsó névben szerepel-e "c" betű (in) .Az eredményt az alábbiak szerint írd ki:
    Az Andrea-ban nem szerepel c betű.
"""
utolso = len(keresztnevek) - 1
if "c" in keresztnevek[utolso].lower():
    print(keresztnevek[utolso], "-ban/-ben található \"c\" betű.")
else:
    print(keresztnevek[utolso], "-ban/-ben nem található \"c\" betű.")
"""
6. Írd ki a neveket csupa nagybetűvel egymás alá (upper()).
"""
i = 0
while (i < len(keresztnevek)):
    print(keresztnevek[i].upper())
    i+=1
