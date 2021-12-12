import time

lefut = False
while (lefut == False):
    try:
        a = int(input("Adjon meg egy számot: "))
        lefut = True
    except:
        print("\nIgazi számot adjon meg!")


lefut = False
while (lefut == False):
    try:
        b = int(input("Adjon meg még egy számot: "))
        lefut = True
    except:
        print("\nIgazi számot adjon meg!")


animation = [
    "[          ]",
    "[=         ]",
    "[==        ]",
    "[===       ]",
    "[====      ]",
    "[=====     ]",
    "[======    ]",
    "[=======   ]",
    "[========  ]",
    "[========= ]",
    "[==========]",
    ]
index = 0


for i in range(len(animation) * 4):
    print(f"Számítás... {animation[index % len(animation)]}", end="\r")
    time.sleep(0.05)
    index+=1
print("")

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} % {b} = {a % b}")
print(f"{a} ^ {b} = {a ** b}")

input("\n\nBEZÁRÁSHOZ: [ENTER]")
