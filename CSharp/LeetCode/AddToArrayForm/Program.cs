using System;
using System.Diagnostics.CodeAnalysis;

class Program
{
    static void Main()
    {
        int[] num = [1, 2, 0, 0];
        int k = 34;
        var result = AddToArrayForm(num, k);
        foreach (int i in result)
        {
            Console.WriteLine(i);
        }
    }

    public static IList<int> AddToArrayForm(int[] num, int k)
    {
        List<int> result = new List<int>();
        int i = num.Length - 1;

        while (i >= 0 || k > 0)
        {
            if (i >= 0)
            {
                k += num[i];
                i--;
            }
            result.Insert(0, k % 10);
            k /= 10;
        }
        return result;
    }
}
