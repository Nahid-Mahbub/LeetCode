using System;
using System.Data;
using System.Diagnostics.Metrics;
using System.Security.Cryptography.X509Certificates;

class Program
{
    static void Main()
    {
        string s = "aAbBcC";
        Console.WriteLine(CountKeyChanges(s));
    }

    public static int CountKeyChanges(string s)
    {
        s= s.ToLower();
        int count = 0;

        for (int i = 1; i < s.Length; i++) {
            if (s[i] != s[i - 1]) {
                count++;
            }
        }
        return count;
    }
}
