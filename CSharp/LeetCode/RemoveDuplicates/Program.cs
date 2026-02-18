using System;

class Program
{
    static void Main()
    {
        int[] nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4];
        Console.WriteLine(RemoveDuplicates(nums));
    }

    public static int RemoveDuplicates(int[] nums)
    {
        int left = 1;
        for (int right = 1; right < nums.Length; right++)
        {
            if (nums[right] != nums[right - 1])
            {
                nums[left] = nums[right];
                left++;
            }
        }
        return left;
    }
}
