"""
1. Feladat:
Kérj be a standard bemenetről egy jelszót. Az elfogadható jelszó: alma, körte, szilva.
Ha helytelen jelszót gépel be a felhasználó, akkor figyelmeztesse a program egy hibaüzenettel.
Amennyiben helyes jelszót gépelt be, akkor üdvözölje gratulációval.
"""

password = input("Adjon meg egy jelszót: ") #BEKÉRÉS
acceptedPasswords = ["alma", "körte", "szilva"] #MEGENGEDETT JELSZAVAK
if password in acceptedPasswords: #HA A BEÍRT JELSZÓ ELEME A LISTÁNAK
    print("A jelszó helyes!")
else:
    print("A jelszó helytelen!")

"""
2. Feladat:
Irass ki minden harmadik számot [1-50] intervallumban for ciklus segítségével.
A számokat egymás mellé, vesszővel elválasztva kell kiíratni.
Az utolsó szám után már ne kerüljön vessző! Ezután írasd ki ugyanezeket a számokat csökkenő sorrendben is!
"""

x = 1 #"JELENLEGI SZÁM"
szamok = [] #SZÁMOK LISTA LÉTREHOZÁSA
while x <= 50: #AMÉG A "JELENLEGI SZÁM" KISEBB VAGY EGYENLŐ 50-NEL, ADDIG:
    szamok.append(x) #"JELENLEGI SZÁM" HOZZÁADÁSA A SZÁMOK LISTÁHOZ
    x+=3 #"JELENLEGI SZÁM" NÖVELÉSE 3-MAL (MERT MINDEN HARMADIK KELL)
print(*szamok, sep=", ") #1-TŐL SZÁMOLVA MINDEN 3. SZÁM KIÍRÁSA VESSZŐVEL ELVÁLASZTVA, AZ UTOLSÓ UTÁN NEM KERÜL VESSZŐ!!
szamok.sort(reverse=True) #SZÁMOK CSÖKKENŐ SORRENDBE TÉTELE
print(*szamok, sep=", ") #SZÁMOK KIÍRÁSA CSÖKKENŐ SORRENDBEN VESSZŐVEL ELVÁLASZTVA, AZ UTOLSÓ UTÁN NEM KERÜL VESSZŐ!!

"""
3. Feladat:
Olvass be pontosan 10 darab egész számot a standard bemenetről.
Írasd ki a képernyőre a megfelelő kísérőszöveggel a számok számtani átlagát, a megfelelő formában.
Ezen felül keresd meg és írasd ki melyik volt a számok közül a legkisebb.
A feladathoz nem használhatsz tömböt, kész függvényeket vagy metódusokat. // ?XD?XD?XD?X?D?XD?XD?X?D?X?D?XD?
"""

#4. PONT FIGYELMEN KÍVÜL HAGYVA! (LISTÁVAL)
x = 1 #BEOLVASOTT DARAB
beolvasottszamok = []
while x <= 10: #AMÉG A BEOLVASÁS KISEBB VAGY EGYENLŐ 10-ZEL, ADDIG:
    kiirtszoveg = "{}. | Adjon meg egy számot: ".format(x) #KIÍRT SZÖVEG
    beolvasottszamok.append(int(input(kiirtszoveg))) #EGÉSZ BEOLVASOTT SZÁM HOZZÁADÁSA A LISTÁHOZ
    x+=1 #BEOLVASOTT DARAB NÖVELÉSE 1-GYEL

#ÁTLÁTHATÓSÁG KEDVÉÉRT:
atlag = sum(beolvasottszamok) / len(beolvasottszamok) #SUM = LISTA MINDEN ÉRTÉKE ÖSSZEADVA, LEN = LISTA HOSSZA[10]
legkisebb = min(beolvasottszamok) #A LISTA LEGKISEBB ÉRTÉKE
print("A beolvasott számok átlaga:", atlag, "~", int(atlag), "\nLegkisebb szám:", legkisebb)

#4. PONT FIGYELEMBEVÉVE
egy = int(input("1. | Adjon meg egy számot: "))
ketto = int(input("2. | Adjon meg egy számot: "))
harom = int(input("3. | Adjon meg egy számot: "))
negy = int(input("4. | Adjon meg egy számot: "))
ot = int(input("5. | Adjon meg egy számot: "))
hat = int(input("6. | Adjon meg egy számot: "))
het = int(input("7. | Adjon meg egy számot: "))
nyolc = int(input("8. | Adjon meg egy számot: "))
kilenc = int(input("9. | Adjon meg egy számot: "))
tiz = int(input("10. | Adjon meg egy számot: "))

atlag = (egy + ketto + harom + negy + ot + hat + het + nyolc + kilenc + tiz) / 10
print("A beolvasott számok átlaga:", atlag, "~", int(atlag))

legkisebb = 0
if egy < ketto and egy < harom and egy < negy and egy < ot and egy < hat and egy < het and egy < nyolc and egy < kilenc and egy < tiz:
    legkisebb = egy
elif ketto < egy and ketto < harom and ketto < negy and ketto < ot and ketto < hat and ketto < het and ketto < nyolc and ketto < kilenc and ketto < tiz:
    legkisebb = ketto
elif harom < egy and harom < ketto and harom < negy and harom < ot and harom < hat and harom < het and harom < nyolc and harom < kilenc and harom < tiz:
    legkisebb = harom
elif negy < egy and negy < ketto and negy < harom and negy < ot and negy < hat and negy < het and negy < nyolc and negy < kilenc and negy < tiz:
    legkisebb = negy
elif ot < egy and ot < ketto and ot < harom and ot < negy and ot < hat and ot < het and ot < nyolc and ot < kilenc and ot < tiz:
    legkisebb = ot
elif hat < egy and hat < ketto and hat < harom and hat < negy and hat < ot and hat < het and hat < nyolc and hat < kilenc and hat < tiz:
    legkisebb = hat
elif het < egy and het < ketto and het < harom and het < negy and het < ot and het < hat and het < nyolc and het < kilenc and het < tiz:
    legkisebb = het
elif nyolc < egy and nyolc < ketto and nyolc < harom and nyolc < negy and nyolc < ot and nyolc < het and nyolc < het and nyolc < kilenc and nyolc < tiz:
    legkisebb = nyolc
elif kilenc < egy and kilenc < ketto and kilenc < harom and kilenc < negy and kilenc < ot and kilenc < het and kilenc < het and kilenc < nyolc and kilenc < tiz:
    legkisebb = kilenc
elif tiz < egy and tiz < ketto and tiz < harom and tiz < negy and tiz < ot and tiz < het and tiz < het and tiz < nyolc and tiz < kilenc:
    legkisebb = tiz
print("A legkisebb:", legkisebb)

"""
4. Feladat:
Tölts fel egy 100 elemű tömböt random egész számokkal [10-50] intervallumból.
Írass ki a képernyőre egy fele akkora tömböt, amelynek az elemeit úgy kapod meg, hogy összeadod az eredeti tömb egymás melletti elemeit.
Tehát pl: uj_tomb[0]=eredeti_tomb[0]+eredeti_tomb[1]; uj_tomb[1]=eredeti_tomb[2]+eredeti_tomb[3]; uj_tomb[2]=eredeti_tomb[4]+eredeti_tomb[5]...
"""

from random import * #RANDOM IMPORTÁLÁSA
x = 1 #LISTA INDEX
szazig = [] #SZÁZIG LISTA LÉTREHOZÁSA
while x <= 100: #AMÉG AZ INDEX KISEBB EGYENLŐ 100-ZAL
    szazig.append(randint(10, 50)) #10, 50 INTERVALLUMBÓL RANDOM SZÁM HOZZÁADÁSA SZÁZIG LISTÁHOZ
    x+=1 #INDEX NÖVELÉSE 1-GYEL

index = 0 #INDEX ALAPÉRTÉKE (SZÁZIG LISTA ELSŐ ÉRTÉKE)
feleakkoralista = [] #FELEAKKORALISTA LÉTREHOZÁSA
while index <= len(szazig) - 1: #AMÉG AZ INDEX KISEBB EGYENLŐ SZÁZIG TÖMB HOSSZÁVAL[100] - 1 = 99, MERT 'xszomszed' EGYEL NÖVELI. => NEM LÉP TÚL A LISTA HOSSZÁN
    xmost = int(szazig[index]) #ELSŐ ÉRTÉK
    xszomszed = int(szazig[index+1]) #MÁSODIK ÉRTÉK
    xhozzaad = int(xmost + xszomszed) #ÉRTÉKEK HOZZÁADÁSA
    feleakkoralista.append(xhozzaad) #ÖSSZEADOTT ÉRTÉK FELE AKKORA LISTÁBA HOZZÁADÁS
    index+=2 #INDEX NÖVELÉSE 2-VEL
print(*feleakkoralista, sep=", ") #FELE AKKORA LISTA KIÍRÁSA VESSZŐVEL ELVÁLASZTVA, UTOLSÓ UTÁN NEM KERÜL VESSZŐ
