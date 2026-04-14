using System;
using System.Data;
using System.Diagnostics.Metrics;

class Program
{
    static void Main()
    {
        int[] nums = [-4, -1, 0, 3, 10];
        foreach(int i in SortedSquares(nums))
        {
            Console.WriteLine(i);
        }

    }

    public static int[] SortedSquares(int[] nums)
    {
        for (int i = 0; i < nums.Length; i++)
        {
            nums[i]= nums[i] * nums[i];
        }
        nums.Sort();

        return nums;
    }
}
