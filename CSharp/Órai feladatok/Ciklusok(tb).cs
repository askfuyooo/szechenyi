using System;
using System.Collections.Generic;

namespace forFeladat
{
    class Program
    {
        static void Main(string[] args)
        {
            /*
            Olvassunk be számokat adott végjelig! A végjel legyen -99.
            Számoljuk meg a páratlan 3-mal osztható számok darabszámát!
            Írjuk képernyore a páros számok szorzatát!


            Kockadobás szimulálás!
            Kérjük be a maximálisan dobható lehetoségek számát! (ez legyen a végjel)
            Számoljuk meg, hogy hányszor dobtunk hatos számot!
            Módosítsuk a programot úgy, hogy ne a felhasználó adja meg a dobás értékét,
            hanem véletlen szám generátorral kapjuk meg a dobás értékét!

            Írj programot, mely beolvas egy pozitív egész számot,
            és kiírja az egész számokat a  képernyőre eddig a számig, egymástól szóközzel elválasztva!

            Írj programot, mely beolvas egy pozitív egész számot,
            és kiírja az egész számokat egymás alá a képernyőre eddig a számig!
            Írj programot, mely beolvas egy pozitív egész számot, és kiírja az osztóit!
            Írj programot, mely beolvas egy pozitív egész számot, és kiírja az osztóinak az összegét!
            Írj programot, mely beolvas egy pozitív egész számot,

            és megmondja, hogy tökéletes szám-e! (A tökéletes számok azok,
            melyek osztóinak összege egyenlő a szám kétszeresével. Ilyen szám pl. a 6, mert 2*6 = 1 + 2 + 3 + 6.)

            Írj programot, mely beolvassa a hatvány alapját és a kitevőt, és kiírja a hatványértéket!
            Határozzuk meg az első N négyzetszám összegét.
            Határozzuk meg egy [a,b] intervallum belsejébe eső négyzetszámokat. 

             */

            int szam = 0;
            bool elfogadva = false;
            List<int> szamok = new List<int>();
            List<int> parosak = new List<int>();
            int paratlan = 0;
            feladatCim(1, "Adjon meg annyi számot, amennyit szeretne. Ha be szeretné fejezni, írjon \"-99\"-t.");
            while (elfogadva == false)
            {
                Console.Write("Adjon meg egy számot: $");
                Console.ForegroundColor = ConsoleColor.Cyan;
                try
                {
                    szam = int.Parse(Console.ReadLine());
                    if (szam != -99)
                    {
                        szamok.Add(szam);

                        if (szam % 3 == 0 && szam % 2 == 0)
                        {
                            paratlan++;
                        }
                        if (szam % 2 == 0)
                        {
                            parosak.Add(szam);
                        }
                    }
                    else
                    {
                        pirossal("A ciklus megszakítása...!");
                        elfogadva = true;
                    }
                }
                catch
                {
                    pirossal("Valódi számot kértem, próbáljuk újra...");
                }
                Console.ForegroundColor = ConsoleColor.White;
            }
            zolddel("A ciklus sikeresen megszakítva!");

            Console.Write("Páratlan, 3-mal osztható számok darabszáma: ");
            Console.ForegroundColor = ConsoleColor.DarkYellow;
            Console.Write($"{paratlan}.\n");
            Console.ForegroundColor = ConsoleColor.White;

            int osszeg = 1;
            foreach (int i in parosak)
            {
                osszeg *= i;
            }

            Console.Write("Páros számok szorzata: ");
            Console.ForegroundColor = ConsoleColor.DarkYellow;
            Console.Write($"{osszeg}.\n");
            Console.ForegroundColor = ConsoleColor.White;

            Console.Write("Ön által megadott számok sorrendben: ");
            Console.ForegroundColor = ConsoleColor.DarkYellow;
            foreach (int i in szamok)
            {
                Console.Write($"{i}; ");
            }
            Console.ForegroundColor = ConsoleColor.White;
            Console.WriteLine();
            ujFeladat(2);
            feladatCim(2, "Kockadobást fogunk szimulálni.\nAz első részben Ön adja meg a dobások számát,\na másodikban véletlenszerűen döntjük el, hányszor dobjuk a kockát.");
            elfogadva = false;
            int dobasok = 0;
            while (elfogadva == false)
            {
                Console.Write("Adja meg a dobások számát: $");
                Console.ForegroundColor = ConsoleColor.Cyan;
                try
                {
                    dobasok = int.Parse(Console.ReadLine());
                    if (dobasok > 0)
                    {
                        zolddel($"Rendben, {dobasok}-szer/-szor fogjuk dobni a kockát.\nA dobások szimulálása az [ENTER] billentyű lenyomása után történik.");
                        elfogadva = true;
                    }
                    else
                    {
                        pirossal("1-nél kevesebbszer nincs sok értelme a dobásnak...");
                    }
                }
                catch
                {
                    pirossal("Valódi számot kértem, próbáljuk újra...");
                }
                Console.ForegroundColor = ConsoleColor.White;
            }

            Random r = new Random();
            int hatosok = 0;
            List<int> dobasokErtekei = new List<int>();
            for (int i = 0; i < dobasok; i++)
            {
                int dobottErtek = r.Next(1, 7);
                dobasokErtekei.Add(dobottErtek);
                if (dobottErtek == 6)
                {
                    hatosok++;
                }
                Console.ForegroundColor = ConsoleColor.Cyan;
                Console.Write("Nyomjon [ENTER]-t a kocka dobásához!");
                Console.ReadLine();
                Console.ForegroundColor = ConsoleColor.DarkGray;
                Console.Write($"A(z) {i + 1}/{dobasok}. dobott érték: ");
                Console.ForegroundColor = ConsoleColor.DarkYellow;
                Console.Write($"{dobottErtek}.");
                Console.WriteLine();
            }
            Console.ForegroundColor = ConsoleColor.Cyan;
            Console.Clear();
            Console.WriteLine("A dobott értékek a következőek:");
            int dobasokDB = 1;
            foreach (int i in dobasokErtekei)
            {
                Console.ForegroundColor = ConsoleColor.DarkGray;
                Console.Write($"A(z) {dobasokDB}/{dobasok} dobás értéke: ");
                Console.ForegroundColor = ConsoleColor.DarkYellow;
                Console.Write($"{i}.\n");
                dobasokDB++;
            }

            if (hatosok == 0)
            {
                pirossal($"Sajnos {dobasok}-ból/-ből egyszer sem sikerült 6-ost dobnia! :(");
            }
            else
            {
                zolddel($"Gratulálunk! Önnek {dobasok}-ból/-ből {hatosok}-szer/-szor sikerült 6-ost dobnia! :)");
            }
            Console.ForegroundColor = ConsoleColor.DarkGray;
            Console.WriteLine("\n--------------------------\n");

            Console.ForegroundColor = ConsoleColor.Blue;
            Console.WriteLine("Rendben, most én döntöm el, hogy hányszor dobjunk...\nGondolok egy számot 1 és 10 között...");
            int ranDob = r.Next(1, 11);
            Console.WriteLine($"Azt mondom, dobjunk {ranDob}-szer/-szor!");
            int ranHatosok = 0;
            List<int> ranDobasokErtekei = new List<int>();
            for (int i = 0; i < ranDob; i++)
            {
                int dobottErtek = r.Next(1, 7);
                ranDobasokErtekei.Add(dobottErtek);
                if (dobottErtek == 6)
                {
                    ranHatosok++;
                }
                Console.ForegroundColor = ConsoleColor.Cyan;
                Console.Write("Nyomjon [ENTER]-t a kocka dobásához!");
                Console.ReadLine();
                Console.ForegroundColor = ConsoleColor.DarkGray;
                Console.Write($"A(z) {i + 1}/{ranDob}. dobott érték: ");
                Console.ForegroundColor = ConsoleColor.DarkYellow;
                Console.Write($"{dobottErtek}.");
                Console.WriteLine();
            }
            Console.ForegroundColor = ConsoleColor.Cyan;
            Console.Clear();
            Console.WriteLine("A dobott értékek a következőek:");
            int ranDobasokDB = 1;
            foreach (int i in ranDobasokErtekei)
            {
                Console.ForegroundColor = ConsoleColor.DarkGray;
                Console.Write($"A(z) {ranDobasokDB}/{ranDob} dobás értéke: ");
                Console.ForegroundColor = ConsoleColor.DarkYellow;
                Console.Write($"{i}.\n");
                ranDobasokDB++;
            }
            if (ranHatosok == 0)
            {
                pirossal($"Sajnos {ranDob}-ból/-ből egyszer sem sikerült 6-ost dobnia! :(");
            }
            else
            {
                zolddel($"Gratulálunk! Önnek {ranDob}-ból/-ből {ranHatosok}-szer/-szor sikerült 6-ost dobnia! :)");
            }

            ujFeladat(3);
            feladatCim(3, "Egy számot fogok kérni, utána segítek elszámolni addig.");

            elfogadva = false;
            szam = 0;
            while (elfogadva == false)
            {
                Console.Write("Adjon meg egy pozitív számot: $");
                Console.ForegroundColor = ConsoleColor.Cyan;
                try
                {
                    szam = int.Parse(Console.ReadLine());
                    if (szam > 0)
                    {
                        zolddel($"Remek, azonnal segítek elszámolni {szam}-ig!");
                        elfogadva = true;
                    }
                    else
                    {
                        pirossal("Pozitív számot kértem, és jó lenne, ha 0 fölött lenne...");
                    }
                }
                catch
                {
                    pirossal("Valódi számot kértem, próbáljuk újra...");
                }
                Console.ForegroundColor = ConsoleColor.White;
            }

            Console.ForegroundColor = ConsoleColor.DarkYellow;
            Console.Write($"Számok {szam}-ig: ");
            Console.ForegroundColor = ConsoleColor.Blue;
            for (int i = 1; i <= szam; i++)
            {
                Console.Write($"{i}; ");
            }
            Console.WriteLine();

            ujFeladat(4);
            feladatCim(4, "Számolni fogunk egy picit pozitív számokkal.\nAdjon meg egy számot, ezzel végzünk pár műveletet.");

            szam = 0;
            elfogadva = false;
            while (elfogadva == false)
            {
                Console.Write("Adjon meg egy számot: $");
                Console.ForegroundColor = ConsoleColor.Cyan;
                try
                {
                    szam = int.Parse(Console.ReadLine());
                    if (szam > 0)
                    {
                        zolddel($"Remek, számoljunk {szam}-val/-vel");
                        elfogadva = true;
                    }
                    else
                    {
                        pirossal("A szám jó lenne, ha nagyobb lenne, mint 0...");
                    }
                }
                catch
                {
                    pirossal("Valódi számot kértem, próbáljuk újra...");
                }
                Console.ForegroundColor = ConsoleColor.White;
            }
            Console.ForegroundColor = ConsoleColor.DarkYellow;
            Console.Write($"Nyomjon [ENTER]-t, és elszámolunk egyesével {szam}-ig!");
            Console.ReadLine();
            Console.ForegroundColor = ConsoleColor.DarkBlue;
            Console.WriteLine($"Számok {szam}-ig:");
            Console.ForegroundColor = ConsoleColor.Blue;

            for (int i = 1; i <= szam; i++)
            {
                Console.WriteLine($"{i};");
            }

            Console.ForegroundColor = ConsoleColor.DarkYellow;
            Console.Write($"Nézzük meg {szam}-nak/-nek az osztóit: ");

            Console.ForegroundColor = ConsoleColor.Blue;

            int osztOsszeg = 0;
            for (int i = 1; i <= szam; i++)
            {
                if (szam % i == 0)
                {
                    Console.Write($"{i}; ");
                    osztOsszeg += i;
                }
            }
            Console.WriteLine();
            Console.ForegroundColor = ConsoleColor.DarkYellow;
            Console.Write("Az osztóinak összege: ");
            Console.ForegroundColor = ConsoleColor.Blue;
            Console.Write($"{osztOsszeg}\n");

            ujFeladat(5);
            feladatCim(5, "Ismeri a tökéletes számokat?\nA tökéletes számok azok, melyek osztóinak összege egyenlő a szám kétszeresével.\nIlyen szám pl. a 6, mert 2*6 = 1 + 2 + 3 + 6.\nIlyet fogunk keresni.");

            szam = 0;
            elfogadva = false;
            while (elfogadva == false)
            {
                Console.Write("Adjon meg egy számot: $");
                Console.ForegroundColor = ConsoleColor.Cyan;
                try
                {
                    szam = int.Parse(Console.ReadLine());
                    if (szam > 0)
                    {
                        zolddel($"Remek, hamarosan ellenőrízhetjük {szam}-ot/-et!");
                        elfogadva = true;
                    }
                    else
                    {
                        pirossal("Jó lenne, ha a szám nagyobb lenne, mint 0...");
                    }
                }
                catch
                {
                    pirossal("Valódi számot kértem, próbáljuk újra...");
                }
                Console.ForegroundColor = ConsoleColor.White;
            }

            Console.ForegroundColor = ConsoleColor.DarkYellow;
            Console.WriteLine($"\n\nNézzük is meg, hogy {szam} tökéletes szám-e!");

            osztOsszeg = 0;
            int ketszeres = 2 * szam;

            for (int i = 1; i <= szam; i++)
            {
                if (szam % i == 0)
                {
                    osztOsszeg += i;
                }
            }

            if (osztOsszeg == ketszeres)
            {
                zolddel($"Gratulálunk! Tökéletes számra ({szam}) lelt!");
            }
            else
            {
                pirossal($"Sajnáljuk, {szam} sajnos nem tökéletes szám!");
            }

            ujFeladat(6);
            feladatCim(6, "Most hatványalapot és -kitevőt fogunk számolni.");


        }




        static void feladatCim(int feladat, string cim)
        {
            Console.Title = $"CIKLUSOK - [{feladat}. Feladat] - TÓTH ÁDÁM 11. F";
            Console.ForegroundColor = ConsoleColor.DarkGray;
            Console.WriteLine($"[{feladat}. Feladat] {cim}");
            Console.ForegroundColor = ConsoleColor.White;
        }
        static void pirossal(string uzenet)
        {
            Console.ForegroundColor = ConsoleColor.DarkRed;
            Console.WriteLine(uzenet);
            Console.ForegroundColor = ConsoleColor.White;
        }
        static void zolddel(string uzenet)
        {
            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine(uzenet);
            Console.ForegroundColor = ConsoleColor.White;
        }
        static void ujFeladat(int feladat)
        {
            Console.ForegroundColor = ConsoleColor.DarkMagenta;
            Console.Write($"\n\n\nA(z) {feladat}. Feladat elindul. Nyomjon [ENTER]-t a folytatáshoz.");
            Console.ForegroundColor = ConsoleColor.White;
            Console.ReadLine();
            Console.Clear();
        }
    }
}
