def animacio(anim):
    import time
    index = 0
    while True:
        print(f"Betöltés... {anim[index % len(anim)]}", end="\r")
        time.sleep(0.1)
        index+=1

animation1 = [
    "[     =     ]",
    "[    = =    ]",
    "[   =   =   ]",
    "[  =     =  ]",
    "[ =       = ]",
    "[=         =]",
    "[ =       = ]",
    "[  =     =  ]",
    "[   =   =   ]",
    "[    = =    ]"
    ]

animation2 = [
    "[           ]",
    "[     =     ]",
    "[    ===    ]",
    "[   =====   ]",
    "[  =======  ]",
    "[ ========= ]",
    "[===========]",
    "[ ========= ]",
    "[  =======  ]",
    "[   =====   ]",
    "[    ===    ]",
    "[     =     ]",
    ]

animation3 = "|/-\\"

error = True
while (error == True):
    choose = input("Animáció száma: ")
    if (choose == "1"):
        error = False
        animacio(animation1)
    elif (choose == "2"):
        error = False
        animacio(animation2)
    elif (choose == "3"):
        error = False
        animacio(animation3)
    """
    elif (choose == "4"):
        error = False
        animacio(animation4)
    """
    else:
        print("\nNem létező animáció!")
