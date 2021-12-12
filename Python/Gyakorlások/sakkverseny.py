"""
Egy sakkversenyen veszel részt. Kérd be a résztvevők számát, majd kérd be minden játékos nevét és pontszámát, és írasd ki a képernyőre.
Továbbjutás 20 pont. Átment/Nem ment át?
"""

resztvevok = int(input("Hány résztvevő van?: "))

i = 0
jatekosok = []
pontszamok = []

while (i < resztvevok):
    jatekosok.append(input(f"{i + 1}. játékos neve: "))
    pontszamok.append(int(input(f"{jatekosok[i]} pontszáma: ")))
    i+=1

i = 0
iras = ""
while (i < resztvevok):
    if (pontszamok[i] >= 20):
        iras = "[továbbjutott]"
    else:
        iras = "[nem jutott tovább]"
    print(f"{jatekosok[i]} pontszáma: {pontszamok[i]} {iras}")
    i+=1
