using System;

class Program
{
    static void Main()
    {
        string s = "abab";
        Console.WriteLine(MaxDistinct(s));
    }

    public static int MaxDistinct(string s)
    {
        HashSet<char> set = new HashSet<char>();
        foreach (char c in s)
        {
            set.Add(c);
        }
        return set.Count;
    }
}
