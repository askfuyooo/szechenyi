elsosor = [" ", " ", " "]
masodiksor = [" ", " ", " "]
harmadiksor = [" ", " ", " "]

def cls():
    import os
    os.system('cls')
    print("Amőba játék v0.3")
    print(f"{elsosor[0]} | {elsosor[1]} | {elsosor[2]}")
    print("----------")
    print(f"{masodiksor[0]} | {masodiksor[1]} | {masodiksor[2]}")
    print("----------")
    print(f"{harmadiksor[0]} | {harmadiksor[1]} | {harmadiksor[2]}")
    print("----------")

cls()

player1name = input("Adja meg \"Játékos1\" nevét: $")
player2name = input("Adja meg \"Játékos2\" nevét: $")

cls()

changePlayer = True
matchIsGoing = True
playerOnGoing = True

moves = []

winnerPlayer = ""

while (matchIsGoing == True):

    oszlop = 0
    sor = 0
    playerOnGoing = True
    currentPlayer = 0
    playerSym = ""
    playerPrint = ""

    if (changePlayer == True):
        currentPlayer = 1
        playerSym = "X"
        playerPrint = player1name
    else:
        currentPlayer = 2
        playerSym = "O"
        playerPrint = player2name

    print(f"{playerPrint} (Játékos{currentPlayer}) [{playerSym}] választ!")
    while (playerOnGoing == True):

        #SOR
        sikeresValasztas = False
        while (sikeresValasztas == False):
            try:
                sor = int(input(f"{playerPrint} sor: $"))
                if (sor >= 1 and sor <= 3):
                    sikeresValasztas = True
                else:
                    print("1 és 3 közötti számot adjon meg!")
            except:
                print("Igazi számot adjon meg!")

        #OSZLOP
        sikeresValasztas = False
        while (sikeresValasztas == False):
            try:
                oszlop = int(input(f"{playerPrint} oszlop: $"))
                if (oszlop >= 1 and oszlop <= 3):
                    sikeresValasztas = True
                else:
                    print("1 és 3 közötti számot adjon meg!")
            except:
                print("Igazi számot adjon meg!")

        tempSor = []
        if (sor == 1):
            tempSor = elsosor
        elif (sor == 2):
            tempSor = masodiksor
        else:
            tempSor = harmadiksor

        tempOszlop = oszlop - 1

        if (tempSor[tempOszlop] == " "):
            tempSor[tempOszlop] = playerSym
            if (sor == 1):
                elsosor = tempSor
            elif (sor == 2):
                masodiksor = tempSor
            else:
                harmadiksor = tempSor

            moves.append(f"JÁTÉKOS{currentPlayer} ({playerSym}) \"{playerPrint}\" LÉPETT -> SOR: {sor} OSZLOP: {oszlop}")

            changePlayer = not changePlayer
            playerOnGoing = False

        else:
            print("A mező már foglalt!")

    
    cls()

    if (elsosor[0] == elsosor[1] and elsosor[1] == elsosor[2] and elsosor[0] != " " and elsosor[1] != " " and elsosor[2] != " "):
        if (elsosor[0] == "X"):
            winnerPlayer = "(Játékos1) [X]"
        else:
            winnerPlayer = "Játékos2 [O]"
        matchIsGoing = False

    elif (masodiksor[0] == masodiksor[1] and masodiksor[1] == masodiksor[2] and masodiksor[0] != " " and masodiksor[1] != " " and masodiksor[2] != " "):
        if (masodiksor[0] == "X"):
            winnerPlayer = "Játékos1 [X]"
        else:
            winnerPlayer = "Játékos2 [O]"
        matchIsGoing = False

    elif (harmadiksor[0] == harmadiksor[1] and harmadiksor[1] == harmadiksor[2] and harmadiksor[0] != " " and harmadiksor[1] != " " and harmadiksor[2] != " "):
        if (harmadiksor[0] == "X"):
            winnerPlayer = "Játékos1 [X]"
        else:
            winnerPlayer = "Játékos2 [O]"
        matchIsGoing = False

    elif (elsosor[0] == masodiksor[0] and masodiksor[0] == harmadiksor[0] and elsosor[0] != " " and masodiksor[0] != " " and harmadiksor[0] != " "):
        if (elsosor[0] == "X"):
            winnerPlayer = "Játékos1 [X]"
        else:
            winnerPlayer = "Játékos2 [O]"
        matchIsGoing = False

    elif (elsosor[1] == masodiksor[1] and masodiksor[1] == harmadiksor[1] and elsosor[1] != " " and masodiksor[1] != " " and harmadiksor[1] != " "):
        if (elsosor[1] == "X"):
            winnerPlayer = "Játékos1 [X]"
        else:
            winnerPlayer = "Játékos2 [O]"
        matchIsGoing = False

    elif (elsosor[2] == masodiksor[2] and masodiksor[2] == harmadiksor[2] and elsosor[2] != " " and masodiksor[2] != " " and harmadiksor[2] != " "):
        if (elsosor[2] == "X"):
            winnerPlayer = "Játékos1 [X]"
        else:
            winnerPlayer = "Játékos2 [O]"
        matchIsGoing = False

    elif (elsosor[0] == masodiksor[1] and masodiksor[1] == harmadiksor[2] and elsosor[0] != " " and masodiksor[1] != " " and harmadiksor[2] != " "):
        if (elsosor[0] == "X"):
            winnerPlayer = "Játékos1 [X]"
        else:
            winnerPlayer = "Játékos2 [O]"
        matchIsGoing = False

    elif (elsosor[2] == masodiksor[1] and masodiksor[1] == harmadiksor[0] and elsosor[2] != " " and masodiksor[1] != " " and harmadiksor[0] != " "):
        if (elsosor[2] == "X"):
            winnerPlayer = "Játékos1 [X]"
        else:
            winnerPlayer = "Játékos2 [O]"
        matchIsGoing = False

    elif (elsosor.count(" ") == 0 and masodiksor.count(" ") == 0 and harmadiksor.count(" ") == 0):
        winnerPlayer = "döntetlen"
        matchIsGoing = False


print("LÉPÉSEK:")

i = 0
while (i < len(moves)):
    print(f"[{i+1}] {moves[i]}")
    i+=1


if (winnerPlayer == "döntetlen"):
    print("\nJáték vége! A játék döntetlen lett!")
else:
    if (winnerPlayer == "Játékos1 [X]"):
        winnername = player1name
    else:
        winnername = player2name
    print(f"\nJáték vége! {winnername} ({winnerPlayer}) nyert!")

#BEZÁRÁS DODGE
input("\n\n\nBEZÁRÁSHOZ NYOMJON [ENTER] GOMBOT!")
