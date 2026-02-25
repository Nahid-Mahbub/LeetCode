using System;

class Program
{
    static void Main()
    {
        string s = "anagram";
        string t = "nagaram";
        Console.WriteLine(IsAnagram(s, t));
    }

    public static bool IsAnagram(string s, string t)
    {
        if(s.Length != t.Length)
        {
            Console.WriteLine("Here");
            return false;
        }

        Dictionary<char, int> forS = new Dictionary<char, int>();
        Dictionary<char, int> forT = new Dictionary<char, int>();

        foreach(char c in s)
        {
            if(forS.ContainsKey(c))
            {
                forS[c]++;
            }
            else
            {
                forS.Add(c, 1);
            }
        }
        foreach(char c in t)
        {
            if(forT.ContainsKey(c))
            {
                forT[c]++;
            }
            else
            {
                forT.Add(c, 1);
            }
        }
        
        foreach(var kvp in forS)
        {
            if (!forT.ContainsKey(kvp.Key) || forT[kvp.Key] != kvp.Value)
            {
                return false;
            }
        }
        return true;
    }
}
