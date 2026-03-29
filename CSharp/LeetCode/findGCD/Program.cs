using System;
using System.Data;

class Program
{
    static void Main()
    {
        int[] nums = [2, 5, 6, 9, 10];
        Console.WriteLine(FindGCD(nums));
    }

    public static int FindGCD(int[] nums)
    {
        int numsMin = nums.Min();
        int numsMax = nums.Max();

        while (numsMin != 0)
        {
            int temp = numsMin;
            numsMin = numsMax % numsMin;
            numsMax = temp;
        }
        return numsMax;
    }
}
