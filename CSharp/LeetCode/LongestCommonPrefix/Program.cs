using System;

class Program
{
    static void Main()
    {
        string[] strs = { "flower", "flow", "flight" };
        Console.WriteLine(LongestCommonPrefix(strs));
    }

    static string LongestCommonPrefix(string[] strs)
    {
        if (strs == null || strs.Length == 0)
            return "";

        if (strs.Length == 1)
            return strs[0];

        for (int i = 0; i < strs[0].Length; i++)
        {
            char currentStr = strs[0][i];

            for (int j = 1; j < strs.Length; j++)
            {
                if (i >= strs[j].Length || strs[j][i] != currentStr)
                {
                    return strs[0].Substring(0, i);
                }
            }
        }
        return strs[0];
    }
}
