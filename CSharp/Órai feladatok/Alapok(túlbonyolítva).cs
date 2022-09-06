using System;

namespace gyakorloFeladat1
{
    class Program
    {
        static void Main(string[] args)
        {
            /*
            1.) Hozzon létre egy 'szoveg' változót, amelynek kezdő értéke legyen: "szia"!
            2.) Kérdezze meg a felhasználó nevét, majd egy 'nev' változóba tárolja el!
            3.) Írja képernyőre a szoveg és a nev változó tartalmát egymás mellé!
		            pl: Szia Peti!
            4.) Hagyjon ki egy üres sort!
            5.) Hozza lérte az alábbi képernyőképet!
                        Iskola: Székesfehérvári SZC 
		                Osztály: 	9F
		                Tanóra: 		Programozás
		                Érdemjegy:    ??????
		   
            6.) Számolja ki egy négyzet kerületét, területét! Írja képernyőre az alábbi formában:
                "A .... oldaló négyzet kerülete: .......
	            területe: ......"
            7.) Számolja ki egy téglalap kerületét, területét! Írja képernyőre az alábbi formában:
                "a oldal: .....				b oldal: ......
                    kerület: .....				terület: .......
            8.) Hozzon létre egy karakterek tárolására alkamas változót!
            9.) Kérjen be egy betűt a felhasználótól, majd írja képernyőre!
            10.) Hozzon létre egy valós számok tárolására alkamas változót! Írja képernyőr az alábbi feladatok eredményét:
                    a.) négyzet oldala * valós változó tartalma
	                b.) téglalap a oldala / négyzet oldala
	                c.) téglalap b oldala / valós változó tartalma
	                d.) téglalap a oldala - téglalap b oldala
	                e.) négyzet a oldalal * 2
	                f.) valós változó tartalma + 5
	 
            11.) Írja képernyőre az összes változó aktuális tartalmát, amit a program írása során felhasznált!
             */

            string szoveg = "Szia";

            Console.Write("Hogy hívnak? $");
            string nev = Console.ReadLine();

            Console.ForegroundColor = ConsoleColor.DarkGray;
            Console.WriteLine($"{szoveg} {nev}!\n");
            Console.ForegroundColor = ConsoleColor.White;

            string iskola, osztaly, tanora;
            double erdemjegy = 1.0;

            Console.Write("Add meg, melyik iskolába jársz: $");
            iskola = Console.ReadLine();
            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine($"Az iskola sikeresen mentve: \"{iskola}\".");
            Console.ForegroundColor = ConsoleColor.White;

            Console.Write("Add meg, melyik osztályba jársz: $");
            osztaly = Console.ReadLine();
            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine($"Az osztály sikeresen mentve: \"{osztaly}\".");
            Console.ForegroundColor = ConsoleColor.White;

            Console.Write("Add meg, melyik tanóra a kedvenced: $");
            tanora = Console.ReadLine();
            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine($"A tanóra sikeresen mentve: \"{tanora}\".");
            Console.ForegroundColor = ConsoleColor.White;

            bool elfogadva = false;
            while (elfogadva == false)
            {
                try
                {
                    Console.Write($"Add meg, hogy {tanora}-ból/-ből hányas lettél év végén: $");
                    erdemjegy = Convert.ToDouble(Console.ReadLine());

                    if (erdemjegy <= 5 && erdemjegy >= 1)
                    {
                        Console.ForegroundColor = ConsoleColor.Green;
                        Console.WriteLine($"Az érdemjegy sikeresen mentve: \"{erdemjegy}\".\n\n");
                        Console.ForegroundColor = ConsoleColor.White;
                        elfogadva = true;
                    }
                    else
                    {
                        Console.ForegroundColor = ConsoleColor.DarkRed;
                        Console.WriteLine("Az érdemjegy nem lehet kisebb, mint 1, vagy nagyobb, mint 5...");
                        Console.ForegroundColor = ConsoleColor.White;
                    }
                }
                catch
                {
                    Console.ForegroundColor = ConsoleColor.DarkRed;
                    Console.WriteLine("Hiba! A lebegőpontos szám megadása helyesen: \"x,y\"...");
                    Console.ForegroundColor = ConsoleColor.White;
                }
            }


            Console.ForegroundColor = ConsoleColor.Cyan;
            Console.WriteLine($"Iskola: \t{iskola}\nOsztály:\t{osztaly}\nTanóra:\t\t{tanora}\nÉrdemjegy:\t{erdemjegy}\n\n");
            Console.ForegroundColor = ConsoleColor.White;
            
            int aNegyzet = 0, aTeglalap = 0, bTeglalap = 0;
            elfogadva = false;
            while (elfogadva == false)
            {
                try
                {
                    Console.Write("Kérem a négyzet \"a\" oldalát: $");
                    aNegyzet = int.Parse(Console.ReadLine());
                    Console.ForegroundColor = ConsoleColor.Green;
                    Console.WriteLine($"A négyzet \"a\" oldala sikeresen mentve: \"{aNegyzet}\".");
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

            elfogadva = false;
            while (elfogadva == false)
            {
                try
                {
                    Console.Write("Kérem a téglalap \"a\" oldalát: $");
                    aTeglalap = int.Parse(Console.ReadLine());
                    Console.ForegroundColor = ConsoleColor.Green;
                    Console.WriteLine($"A téglalap \"a\" oldala sikeresen mentve: \"{aTeglalap}\".");
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

            elfogadva = false;
            while (elfogadva == false)
            {
                try
                {
                    Console.Write("Kérem a téglalap \"b\" oldalát: $");
                    bTeglalap = int.Parse(Console.ReadLine());
                    Console.ForegroundColor = ConsoleColor.Green;
                    Console.WriteLine($"A téglalap \"b\" oldala sikeresen mentve: \"{bTeglalap}\".");
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

            Console.WriteLine($"A(z) {aNegyzet}cm oldalú négyzet kerülete: {4 * aNegyzet}cm\nterülete: {aNegyzet * aNegyzet}cm^2\n\n");
            Console.WriteLine($"a oldal: {aTeglalap}cm\tb oldal: {bTeglalap}cm\nkerület: {2 * (aTeglalap + bTeglalap)}cm\tterület: {aTeglalap * bTeglalap}cm^2\n\n");

            char karakter = 'a';
            elfogadva = false;
            while (elfogadva == false)
            {
                try
                {
                    Console.Write("Kérek egy karaktert: $");
                    karakter = Convert.ToChar(Console.ReadLine());
                    Console.ForegroundColor = ConsoleColor.Green;
                    Console.WriteLine($"A megadott karakter a(z) \"{karakter}\".\n\n");
                    Console.ForegroundColor = ConsoleColor.White;
                    elfogadva = true;
                }
                catch
                {
                    Console.ForegroundColor = ConsoleColor.DarkRed;
                    Console.WriteLine("Egy darab karaktert kértem, próbáljuk újra...");
                    Console.ForegroundColor = ConsoleColor.White;
                }
            }

            int szam = 0;

            elfogadva = false;
            while (elfogadva == false)
            {
                try
                {
                    Console.Write("Kérek egy valós számot: $");
                    szam = int.Parse(Console.ReadLine());
                    Console.ForegroundColor = ConsoleColor.Green;
                    Console.WriteLine($"A valós szám sikeresen mentve: \"{szam}\".");
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

            Console.WriteLine($"a) {aNegyzet} * {szam} = {aNegyzet * szam}\nb) {aTeglalap} / {aNegyzet} = {aTeglalap / aNegyzet}\nc) {bTeglalap} / {szam} = {bTeglalap / szam}\nd) {aTeglalap} - {bTeglalap} = {aTeglalap - bTeglalap}\ne) {aNegyzet} * 2 = {aNegyzet * 2}\nf) {szam} + 5 = {szam + 5}");

            Console.WriteLine($"\n\nA program során felhasznált változók:\nszoveg(string): {szoveg}\nnev(string): {nev}\nelfogadva(bool): {elfogadva}\niskola(string): {iskola}\nosztaly(string): {osztaly}\ntanora(string): {tanora}\nerdemjegy(double): {erdemjegy}\naNegyzet(int): {aNegyzet}\naTeglalap(int): {aTeglalap}\nbTeglalap(int): {bTeglalap}\nkarakter(char): {karakter}\nszam(int): {szam}");


            //BEZÁRÁS DODGE
            Console.Write("\n\nBezáráshoz nyomjon [ENTER] billentyűt!");
            Console.ReadLine();
        }
    }
}
