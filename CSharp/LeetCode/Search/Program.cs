using System;

class Program
{
    static void Main()
    {
        int[] nums = [4, 5, 6, 7, 0, 1, 2];
        int target = 0;
        Console.WriteLine(Search(nums, target));
    }

    public static int Search(int[] nums, int target)
    {
        if (nums.Contains(target))
            return nums.IndexOf(target);
        else
            return -1;
    }
}
