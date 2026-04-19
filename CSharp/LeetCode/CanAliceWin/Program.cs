using System;
using System.Data;
using System.Diagnostics.Metrics;

class Program
{
    static void Main()
    {
        int[] nums = {1, 2, 3, 4, 10};
        Console.WriteLine(CanAliceWin(nums));
    }

    public static bool CanAliceWin(int[] nums)
    {
        int singleNum = 0;
        int doubleNum = 0;
        foreach (int i in nums)
        {
            if (i < 10)
            {
                singleNum += i;
            }
            else
            {
                doubleNum += i;
            }
        }
        return singleNum == doubleNum ? false : true;
    }
}
