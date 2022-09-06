using System;

namespace masodikGyak
{
    class Program
    {
        static void Main(string[] args)
        {
            /*  
            1. Kérjen be egy számot, majd döntse el a számról, hogy páros és pozitív vagy páratlan és negatív!


            2. Hozzon létre egy karakter tárolására alkalmas változót. Amennyiben a felhasználó 'k' vagy 'K' betut üt le, 
            a program az alábbi választási lehetoséget kínálja:
            "Négyzet vagy téglalap kerületét szeretné kiszámítani? Válasszon: n/t"
            Amennyiben 'n' betut választott, számítsa ki a négyzet kerületét,
            ha pedig 't' betut, akkor a téglalap kerületét! Az oldalhosszúságot a felhasználó adja meg.


            3. Kérjen be egy számot, majd döntse el a számról, hogy páros és pozitív vagy páratlan és negatív!


            4. Vegyen fel egy 'szam2' valtozót, melynek típusa megegyezik a 3. feladatban használt változó típusával.
            Írja képernyore a két számmal végezheto alapmuveletek eredményeit!
             */

            bool elfogadva = false;
            int szam = 0;

            while (elfogadva == false)
            {
                try
                {
                    Console.Write("Adjon meg egy számot: $");
                    szam = int.Parse(Console.ReadLine());
                    Console.ForegroundColor = ConsoleColor.Green;
                    Console.WriteLine($"A szám mentve \"{szam}\" értékkel.");
                    Console.ForegroundColor = ConsoleColor.White;
                    elfogadva = true;
                }
                catch
                {
                    Console.ForegroundColor = ConsoleColor.DarkRed;
                    Console.WriteLine("Valós számot kértem, próbáljuk újra...");
                    Console.ForegroundColor = ConsoleColor.White;
                }
            }

            Console.ForegroundColor = ConsoleColor.Yellow;
            if (szam > 0 && szam % 2 == 0)
            {
                Console.WriteLine("A szám páros és pozitív");
            }
            else if (szam < 0 && szam % 2 != 0)
            {
                Console.WriteLine("A szám páratlan és negatív");
            }
            else
            {
                Console.WriteLine("A szám nem páros és pozitív, illetve nem páratlan és negatív.");
            }
            Console.ForegroundColor = ConsoleColor.White;


            char valasz;
            elfogadva = false;
            while (elfogadva == false)
            {
                try
                {
                    Console.Write("Válasszon, hogy területet, vagy kerületet szeretne számítani. [k/t] $");
                    valasz = Convert.ToChar(Console.ReadLine());
                    if (valasz == 'k' || valasz == 'K')
                    {
                        elfogadva = true;
                    }
                    else if (valasz == 't' || valasz == 'T')
                    {
                        elfogadva = true;
                    }
                    else
                    {
                        Console.ForegroundColor = ConsoleColor.DarkRed;
                        Console.WriteLine("Kerületet(k), vagy területet(t) kértem, próbáljuk újra...");
                        Console.ForegroundColor = ConsoleColor.White;
                    }
                }
                catch
                {
                    Console.ForegroundColor = ConsoleColor.DarkRed;
                    Console.WriteLine("Egy darab karaktert kértem, próbáljuk újra...");
                    Console.ForegroundColor = ConsoleColor.White;
                }
            }
        }
    }
}
