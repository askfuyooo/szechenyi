using System;

namespace MultiReadLine
{
    class Program
    {
        static void Main(string[] args)
        {
            while (true)
                {
                Console.Write("> ");
                string[] Lines = Console.ReadLine().Split(' ');
                if (Lines[0] == "run")
                {
                    if (Lines.Length == 2)
                    {
                        if (Lines[1] == "vsc")
                        {
                            Console.WriteLine("Visual Studio Code");
                        }
                        else if (Lines[1] == "cmd")
                        {
                            Console.WriteLine("Command Promt");
                        }
                        else
                        {
                            Console.WriteLine("ERROR!");
                        }
                    }
                    else
                    {
                        Console.WriteLine("ERROR!");
                    }
                }
                else
                {
                    Console.WriteLine("ERROR!");
                }
            }
        }
    }
}
