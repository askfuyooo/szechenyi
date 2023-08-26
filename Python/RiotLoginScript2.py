from getpass import getpass
from os import system, path, makedirs, listdir, remove
from time import sleep
import shutil

folder_name = "LAM_Accounts"
documents = path.expanduser("~\\Documents")
lamcontainer = path.join(documents, folder_name)

accounts = []
regions = ["br", "eune", "euw", "lan", "las", "na", "oce", "ru", "tr", "jp", "kr", "ph", "sg", "tw", "th", "vn", "pbe"]

def LIBARYTEST():
    system("title LAM-CHECK Pyautogui and Keyboard libary check")
    try:
        import pyautogui
    except:
        system("py -m pip install pyautogui")
        try:
            import pyautogui
        except:
            input("[LAM-ERR] Installation error!\nIf LAM can't start, write 'pip install pyautogui' or 'py -m pip install pyautogui' in cmd!\nPress [ENTER] to close.")
            exit()
    try:
        import keyboard
    except:
        system("py -m pip install keyboard")
        try:
            import keyboard
        except:
            input("[LAM-ERR] Installation error!\nIf LAM can't start, write 'pip install keyboard' or 'py -m pip install keyboard' in cmd!\nPress [ENTER] to close.")
            exit()

    print("[LOL ACCOUNT MANAGER] Testing pyautogui")
    try:
        pyautogui.moveTo(0, 0)
        print("[LOL ACCOUNT MANAGER] pyautogui succeed")
    except:
        input("[LAM-ERR] pyautogui error.\nPress [ENTER] to close.")
        exit()

    sleep(0.5)
    CLS()

def listAccounts():
    accounts.clear()
    files = listdir(lamcontainer)
    i = 0
    for file in files:
        with open(f"{lamcontainer}\{file}", "r") as f:
            lines = f.readlines()
            print(f"[{i + 1}] {file} ({lines[1]})")
        i += 1
        accounts.append(file)

def CLS():
    system("cls")

class User:
    def __init__(self, username, password, region):
        self.username = username
        self.password = password
        self.region = region

LIBARYTEST()
running = True
while (running):
    system("title League of Legends Account Manager 2 by Fuyooo - OPEN SOURCE")
    print(f"LAM Path: {lamcontainer}")
    print("Please select an option!")
    print("[1] Login into an account\n[2] Register new account\n[3] Delete account\n[4] Reset LAM\n[5] Quit LAM")

    selected = False
    while (selected == False):
        choice = 0
        try:
            choice = int(input("Option selected: $"))
            if (choice >= 1 and choice <= 5):
                selected = True
            else:
                print("Selected option should be between 1 and 5! Try again!")
        except:
            print("You should select an existing option! Try again!")

    if (selected):
        if not path.exists(lamcontainer):
            makedirs(lamcontainer)

        if (choice == 1):
            CLS()
            system("title LAM Account login")
            print("Select an account you want to log in")
            try:
                listAccounts()
            except:
                print("[LAM-ERR] An error occured while listing accounts!")
            if (len(accounts) >= 1):
                selected = False
                while not (selected):
                    choice = 0
                    try:
                        choice = int(input("Which account you want to log in? $"))
                        if (choice <= len(accounts) and choice >= 1):
                            username = accounts[choice - 1]
                            selected = True
                        else:
                            print("[LAM-ERR] Account does not exists! Try again!") 
                    except:
                        print("[LAM-ERR] Account does not exists! Try again!")

                userdata = []                
                with open(f"{lamcontainer}\{username}", "r") as f:
                    userdata = f.readlines()
                user = User(username, userdata[0], userdata[1])
                userdata.clear()
                
                CLS()
                print(f"Selected account: {user.username}. Click on the username field in LOL Client.\nPress R to log in.\nPress E to exit.")
                import pyautogui
                from keyboard import is_pressed
                waiting = True
                while (waiting):
                    if (is_pressed('R')):
                        print("Logging in...")
                        sleep(0.5)
                        pyautogui.press("BACKSPACE")
                        pyautogui.write(user.username)
                        pyautogui.press("TAB")
                        pyautogui.write(user.password)
                        for i in range(5):
                            pyautogui.press("TAB")
                        pyautogui.press("ENTER")
                        pyautogui.press("TAB")
                        pyautogui.press("ENTER")
                        print("Logged in! Quitting LAM...")
                        sleep(1)
                        exit()
                        waiting = False
                    elif (is_pressed('E')):
                        print("Aborting login...")
                        sleep(0.5)
                        pyautogui.press("BACKSPACE")
                        sleep(1.5)
                        waiting = False
            else:
                print("[LAM-ERR] There are no registered accounts!")
                sleep(1.5)
            CLS()

        elif (choice == 2):
            CLS()
            system("title LAM Account register")
            print("Register the account in League of Legends Account Manager")
            empty = True
            while (empty):
                name = input("Account name: $")
                if (len(name) <= 3):
                    print("[LAM-ERR] Account name length cannot be less than 3!")
                else:
                    empty = False

            empty = True
            while (empty):
                password = getpass("Account password: $")
                if (len(password) <= 3):
                    print("[LAM-ERR] Account password length cannot be less than 3!")
                else:
                    empty = False

            rExist = False
            while not (rExist):
                region = input("Account region: $").lower()
                if (region not in regions):
                    print("Region does not exists!")
                else:
                    rExist = True
            user = User(name, password, region)
            try:
                target = f"{lamcontainer}\{user.username}"
                if not (path.exists(target)):
                    with open(target, "w") as f:
                        f.write(user.password + "\n")
                        f.write(user.region)
                        print(f"Account successfully registered! ({target})")
                else:
                    print("[LAM-ERR] Account already registered!")
            except:
                print("[LAM-ERR] Account cannot be registered!")
            sleep(1.5)
            CLS()
        elif (choice == 3):
            CLS()
            system("title LAM Account remover")
            print("Remove the account from League of Legends Account Manager")
            try:
                listAccounts()
            except:
                print("[LAM-ERR] An error occured while listing accounts!")
            if (len(accounts) >= 1):
                selected = False
                while not (selected):
                    choice = 0
                    try:
                        choice = int(input("Which account you want to remove? $"))
                        if (choice <= len(accounts) and choice >= 1):
                            user = accounts[choice - 1]
                            confirmed = False
                            selected = True
                            while not (confirmed):
                                confirm = input(f"Are you sure want to remove account {user}? [y/n] $").lower()
                                if (confirm == "y"):
                                    target = f"{lamcontainer}\{user}"
                                    if (path.exists(target)):
                                        remove(target)
                                        print(f"Account {user} successfully removed! ({target})")
                                        confirmed = True
                                    else:
                                        print(f"Account {user} disappeared from files!")
                                    sleep(1.5)
                                elif (confirm == "n"):
                                    confirmed = True
                                    print("Account was not removed!")
                                    sleep(1.5)
                                else:
                                    print("[LAM-ERR] Please answer 'y' or 'n'!")
                        else:
                            print("[LAM-ERR] Account does not exists! Try again!") 
                    except:
                        print("[LAM-ERR] Account does not exists! Try again!")
            else:
                print("[LAM-ERR] There are no registered accounts!")
                sleep(1.5)
            CLS()

        elif (choice == 4):
            confirmed = False
            while not (confirmed):
                confirm = input("Are you sure want to reset LAM? [y/n] $").lower()
                if (confirm == "y"):
                    print("Resetting LAM...")
                    confirmed = True
                    try:
                        shutil.rmtree(lamcontainer)
                        print("LAM reset was successful!")
                    except:
                        print("LAM reset failed!")
                    sleep(1.5)
                    CLS()
                elif (confirm == "n"):
                    confirmed = True
                    CLS()
                else:
                    print("[LAM-ERR] Please answer 'y' or 'n'!")
        elif (choice == 5):
            print("LAM quitting safely...")
            sleep(1)
            exit()
        else:
            print("An unexpected error occured!")
            input("Press [ENTER] to exit!")
            exit()
