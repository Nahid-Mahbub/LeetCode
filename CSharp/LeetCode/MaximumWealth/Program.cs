using System;
using System.Data;
using System.Diagnostics.Metrics;

class Program
{
    static void Main()
    {
        int[][] accounts = [[2, 8, 7], [7, 1, 3], [1, 9, 5]];
        Console.WriteLine(MaximumWealth(accounts));
    }

    public static int MaximumWealth(int[][] accounts)
    {
        int maxWealth = 0;
        foreach (int[] account in accounts)
        {
            if(maxWealth < account.Sum()) {
                maxWealth = account.Sum();
            }
        }
        return maxWealth;
    }
}
