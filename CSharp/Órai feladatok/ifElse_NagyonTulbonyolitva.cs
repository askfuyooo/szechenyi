using System;

namespace ifElse
{
    class Program
    {
        static void Main(string[] args)
        {
            /*
             1. Írjunk programot, mely a testsúly és a testmagasság
            alapján meghatározza a testtömegindexet, és kiírja, hogy milyen testsúly osztályba
            tartozik az adott illető. a testtömeg osztályokat meghatározhatjuk tetszőlegesen,
            de alapul vehetünk létező osztályozásokat is.
            Testtomegindex = Testtomeg[kg]/testmagassg2[m]
            <16 súlyos soványság
            16-17 mérsékelt soványság
            17-18.5 enyhe soványság
            18.5-25 normális tetssúly
            25-30 túlsúlyos
            >30 elhízott

            2. Készítsünk programot, amely bekéri a víz hőmérsékletét,
            majd eldönti, hogy az milyen halmazállapotú. A halmazállapot lehet folyékony,
            gőz, vagy jég.


            3. Írjon egy programot, ami leosztályoz egy maximálisan
            100 pontos dolgozatot az 50, 65, 80, 90 ponthatárok szerint! A határérték a jobb jegyhez
            tartozik. Ha a pontszám negatív vagy száznál nagyobb, akkor a program írja ki, hogy
            hibás az adat!
             */

            //1. Feladat
            Console.Title = "[1. Feladat] Testtömegindex Kalkulátor";

            Console.WriteLine("Üdvözöljük a BMI Kalkulátorban!");

            bool elfogadva = false;
            int testtomeg = 0;
            double testmagassag = 0, testtomegindex = 0;

            while (elfogadva == false)
            {
                Console.ForegroundColor = ConsoleColor.DarkGray;
                Console.Write("Kérem adja meg a testtömegét kilogramban mérve: $");
                try
                {
                    testtomeg = int.Parse(Console.ReadLine());
                    Console.ForegroundColor = ConsoleColor.Green;
                    Console.WriteLine($"Az Ön testtömege sikeresen mentve! ({testtomeg}kg)");
                    Console.ForegroundColor = ConsoleColor.White;
                    elfogadva = true;
                }
                catch
                {
                    Console.ForegroundColor = ConsoleColor.DarkRed;
                    Console.WriteLine("Valós számot adjon meg, próbáljuk újra...");
                }
            }

            elfogadva = false;
            while (elfogadva == false)
            {
                Console.ForegroundColor = ConsoleColor.DarkGray;
                Console.Write("Kérem adja meg a testmagasságát méterben mérve: $");
                try
                {
                    testmagassag = Convert.ToDouble(Console.ReadLine());
                    Console.ForegroundColor = ConsoleColor.Green;
                    Console.WriteLine($"Az Ön testmagassága sikeresen mentve! ({testmagassag}m)");
                    Console.ForegroundColor = ConsoleColor.White;
                    elfogadva = true;
                }
                catch
                {
                    Console.ForegroundColor = ConsoleColor.DarkRed;
                    Console.WriteLine("Lebegőpontos számot adjon meg, vesszővel elválasztva, próbáljuk újra...");
                }
            }

            Console.Clear();
            Console.ForegroundColor = ConsoleColor.Cyan;
            Console.WriteLine($"Az Ön testtömege: {testtomeg}kg\nAz Ön testmagassága: {testmagassag}m");

            Console.ForegroundColor = ConsoleColor.Yellow;
            Console.WriteLine("\nA testtömegindex kiszámítási képlete: testtömeg/testmagasság^2");
            testtomegindex = testtomeg / (testmagassag * testmagassag);
            Console.WriteLine($"{testtomeg} / {testmagassag}^2 = {testtomegindex}");

            Console.ForegroundColor = ConsoleColor.Cyan;
            Console.WriteLine($"\nAz Ön testtömegindexe pontosan {testtomegindex}.");

            string bmiErtek = "";
            string[] ertekek = { "súlyos soványság \t| <16", "mérsékelt soványság \t| 16-17", "enyhe soványság \t| 17-18.5", "normális testsúly \t| 18.5-25", "túlsúlyos \t\t| 25-30", "elhízott \t\t| >30" };

            if (testtomegindex < 16)
            {
                bmiErtek = ertekek[0];
            }
            else if (testtomegindex > 16 && testtomegindex < 17)
            {
                bmiErtek = ertekek[1];
            }
            else if (testtomegindex > 17 && testtomegindex < 18.5)
            {
                bmiErtek = ertekek[2];
            }
            else if (testtomegindex > 18.5 && testtomegindex < 25)
            {
                bmiErtek = ertekek[3];
            }
            else if (testtomegindex > 25 && testtomegindex < 30)
            {
                bmiErtek = ertekek[4];
            }
            else
            {
                bmiErtek = ertekek[5];
            }

            Console.WriteLine("Az ön egészségcsoportja a testtömegindexe alapján:");
            foreach (string i in ertekek)
            {
                Console.ForegroundColor = ConsoleColor.DarkRed;
                if (bmiErtek == i)
                {
                    Console.ForegroundColor = ConsoleColor.Green;
                }
                Console.WriteLine(i);
            }

            //1. Feladat vége
            Console.ForegroundColor = ConsoleColor.White;
            Console.Write("\n\nA 2. feladat indításához nyomjon [ENTER] billentyűt!");
            Console.ReadLine();
            Console.Clear();


            //2. Feladat
            Console.Title = "[2. Feladat] Halmazállapot Kalkulátor";
            Console.WriteLine("Üdvözöljük a Halmazállapot Kalkulátorban!");

            elfogadva = false;
            int homerseklet = 0;
            while (elfogadva == false)
            {
                Console.ForegroundColor = ConsoleColor.DarkGray;
                Console.Write("Kérem adja meg a víz hőmérsékletét Celsius fokban: $");
                try
                {
                    homerseklet = int.Parse(Console.ReadLine());
                    Console.ForegroundColor = ConsoleColor.Green;
                    Console.WriteLine($"A víz hőmérséklete sikeresen mentve! ({homerseklet}°C)");
                    Console.ForegroundColor = ConsoleColor.Cyan;
                    elfogadva = true;
                }
                catch
                {
                    Console.ForegroundColor = ConsoleColor.DarkRed;
                    Console.WriteLine("Egész számot adjon meg, próbáljuk újra...");
                }
            }

            string halmazallapot = "";
            if (homerseklet <= 0)
            {
                halmazallapot = "jég";
            }
            else if (homerseklet < 100)
            {
                halmazallapot = "folyékony";
            }
            else
            {
                halmazallapot = "gőz";
            }

            Console.WriteLine($"\nA víz hőmérséklete {homerseklet}°C, ezért halmazállapota {halmazallapot}.");

            //2. Feladat vége
            Console.ForegroundColor = ConsoleColor.White;
            Console.Write("\n\nA 3. feladat indításához nyomjon [ENTER] billentyűt!");
            Console.ReadLine();
            Console.Clear();


            //3. Feladat
            Console.Title = "[3. Feladat] Dolgozat érdemjegy Kalkulátor";
            Console.WriteLine("Üdvözöljük a Dolgozat érdemjegy Kalkulátorban!");
            Console.WriteLine("A dolgozat maximális pontszáma 100.");

            int eredmeny = 0;
            elfogadva = false;
            while (elfogadva == false)
            {
                Console.ForegroundColor = ConsoleColor.DarkGray;
                Console.Write("Adja meg a dolgozat pontszámát: $");
                try
                {
                    eredmeny = int.Parse(Console.ReadLine());
                    if (eredmeny >= 0 && eredmeny <= 100)
                    {
                        Console.ForegroundColor = ConsoleColor.Green;
                        Console.WriteLine($"A dolgozat pontszáma sikeresen mentve! {eredmeny}");
                        Console.ForegroundColor = ConsoleColor.Cyan;
                        elfogadva = true;
                    }
                    else
                    {
                        Console.ForegroundColor = ConsoleColor.DarkRed;
                        Console.WriteLine("A dolgozat pontszáma nem lehet kisebb, mint 0, vagy nagyobb, mint 100, próbáljuk újra...");
                    }
                }
                catch
                {
                    Console.ForegroundColor = ConsoleColor.DarkRed;
                    Console.WriteLine("Valós számot adjon meg, próbáljuk újra...");
                }
            }

            int erdemjegy = 0;

            if (eredmeny >= 90)
            {
                erdemjegy = 5;
            }
            else if (eredmeny >= 80)
            {
                erdemjegy = 4;
            }
            else if (eredmeny >= 65)
            {
                erdemjegy = 3;
            }
            else if (erdemjegy >= 50)
            {
                erdemjegy = 2;
            }
            else
            {
                erdemjegy = 1;
            }

            Console.WriteLine($"A tanuló {eredmeny}/100 pontot ért el, {eredmeny}%-os eredménnyel, érdemjegye: {erdemjegy}.");

            //3. Feladat vége
            Console.ForegroundColor = ConsoleColor.White;
            Console.Write("\n\nA 3. feladat bezárásához nyomjon [ENTER] billentyűt!");
            Console.ReadLine();
            Console.Clear();

            //ÖSSZEFOGLALÓ
            Console.Title = "[VÉGE] Összefoglaló";
            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine("A program sikeresen lefutott hiba nélkül! :)");
            Console.ForegroundColor = ConsoleColor.White;
            Console.Write("\n\nBezáráshoz nyomjon [ENTER] gombot!");
            Console.ReadLine();
        }
    }
}
