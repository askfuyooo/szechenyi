password = input("Adjon meg egy 4 számjegyű PIN kódot: ")
password = int(password)
print("Kód mentve.")

success = False
passTest = 0
while success == False:
    passTest = input("Kérem, adja meg a jelszót: ")
    passTest = int(passTest)
    if passTest == password:
        print("Success. Password was", passTest)
        success = True
