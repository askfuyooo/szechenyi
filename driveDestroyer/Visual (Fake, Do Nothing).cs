using System;
using System.IO;
using System.Threading;

namespace chrmUpdtr
{
    class Program
    {
        static void Main(string[] args)
        {
            int status = 0;
            Console.Title = "\tChromeUpdater | Downloading assets...";
            Console.ForegroundColor = ConsoleColor.DarkGray;
            Console.Write("[1] Status: "); Console.ForegroundColor = ConsoleColor.Cyan;
            Console.Write("Request Update Permissions...\n");
            Console.ForegroundColor = ConsoleColor.DarkGray;
            Console.Write("[2] Status: "); Console.ForegroundColor = ConsoleColor.Green;
            Console.Write("Access Granted...\n");
            Random r = new Random();
            int random = r.Next(11, 101);
            int randomDownloadSpeed = 500;
            for (int i = 3; i < random; i++)
            {
                randomDownloadSpeed = r.Next(500, 3001);
                Console.ForegroundColor = ConsoleColor.DarkGray;
                Console.Write("[{0}] Status: ", i);
                Console.ForegroundColor = ConsoleColor.Cyan;
                Console.Write("Downloading assets... {0} / {1}\n", i-2, random-3);           
                Thread.Sleep(randomDownloadSpeed);
                status = i;
            }

            Console.ForegroundColor = ConsoleColor.DarkGray;
            status++;
            Console.Title = "\tChromeUpdater | Installing assets...";
            
            for (int i = 3; i < random; i++)
            {
                randomDownloadSpeed = r.Next(250, 1000);
                Console.ForegroundColor = ConsoleColor.DarkGray;
                Console.Write("[{0}] Status: ", status++); Console.ForegroundColor = ConsoleColor.Cyan;
                Console.Write("Installing assets... {0} / {1}\n", i-2, random-3);
                Thread.Sleep(randomDownloadSpeed);
            }

            Thread.Sleep(1000);
            Console.ForegroundColor = ConsoleColor.Green;
            Console.Title = "\tChromeUpdater | Successfully Updated";
            Console.WriteLine("Chrome is successfully updated! Enjoy!");
            Console.ForegroundColor = ConsoleColor.White;
            Console.WriteLine("Press [ANY] key to exit.");
            Console.ReadKey();
        }
    }
}
