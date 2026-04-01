using System;
using System.Data;

class Program
{
    static void Main()
    {
        int n = 3;
        int[] startPos = [0, 1];
        string s = "RRDDLU";
         foreach (int i in ExecuteInstructions(n, startPos, s))
        {
            Console.WriteLine(i);
        }
    }

    public static int[] ExecuteInstructions(int n, int[] startPos, string s)
    {
        return new int[] { 0, 1, 2 };
    }
}
