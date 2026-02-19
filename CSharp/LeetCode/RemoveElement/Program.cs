using System;
using System.Diagnostics.Metrics;

class Program
{
    static void Main()
    {
        int[] nums = [3, 2, 2, 3];
        int val = 3;
        Console.WriteLine(RemoveElement(nums, val));
    }

    public static int RemoveElement(int[] nums, int val)
    {
        int left = 0;
        for (int i = 0; i < nums.Length; i++)
        {
            if(nums[i] != val)
            {
                nums[left] = nums[i];
                left++;
            }
        }
        return left;

    }
}
