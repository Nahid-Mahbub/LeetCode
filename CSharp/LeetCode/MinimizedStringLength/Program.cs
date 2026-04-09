using System;
using System.Data;
using System.Diagnostics.Metrics;

class Program
{
    static void Main()
    {
        string s = "aaabc";
        Console.WriteLine(MinimizedStringLength(s));
    }

    public static int MinimizedStringLength(string s)
    {
        HashSet<char> chr = new HashSet<char>(s);
        //foreach (char c in s)
        //{
        //    chr.Add(c);
        //}
        return chr.Count();
    }
}
