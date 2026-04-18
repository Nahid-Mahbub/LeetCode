using System;
using System.Data;
using System.Diagnostics.Metrics;

class Program
{
    static void Main()
    {
        int[] nums = { 9, 72, 34, 29, -49, -22, -77, -17, -66, -75, -44, -30, -24 };
        Console.WriteLine(ArraySign(nums));
    }

    public static int ArraySign(int[] nums)
    {
        if (nums.Contains(0))
            return 0;

        int productSign = 1;
        foreach (int num in nums)
        {
            if (num > 0)
                productSign *= 1;
            else
                productSign *= -1;
        }
        return productSign;
    }
}
