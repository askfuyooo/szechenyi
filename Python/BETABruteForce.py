import time

password = input("Jelszó: ")
passInt = int(password)
print(password)
time.sleep(1)

tryPass = 1000
success = False
while success == False:
    if tryPass < 10000:
        if tryPass == passInt:
            print("Success. Password was", tryPass,end="" ".")
            success = True
        else:
            tryPass = tryPass + 1
            print("[BF] | CURRENT PASS:", tryPass)
    else:
        print("Unsuccess.")
        success = True
