using System;
					
public class Program
{
	public static void Main()
	{
		while (true)
		{
		Console.Write("root#>");
		string[] args = Console.ReadLine().ToLower().Split(' ');
		switch (args[0])
		{
			case "run":
				{
					try {
switch (args[1])
{
	case "cmd":
		{
			Console.WriteLine("Command Promt");
break;
		}
	default:
		{
Console.WriteLine("Nincs 2. arg.");
			break;
		}
}
} 
catch {
	Console.WriteLine("Run what? :)");
}
					break;
				}
				default: 
			{
			Console.WriteLine("?");
			break;
		}
		}
		}
	}
}
