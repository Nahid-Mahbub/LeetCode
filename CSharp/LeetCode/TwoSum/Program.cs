using System;

class Program
{
    static void Main()
    {
        int[] nums = [2, 7, 11, 15];
        int target = 9;
        //Console.WriteLine(Intersection(nums1, nums2));
        foreach (int x in TwoSum(nums, target))
        {
            Console.WriteLine(x);
        }
    }

    public static int[] TwoSum(int[] nums, int target)
    {
        for (int i = 0; i < nums.Length; i++)
        {
            for (int j = i + 1; j < nums.Length; j++)
            {
                if (nums[i] + nums[j] == target)
                {
                    return new int[] { i, j};
                }
            }
        }
        return null;
    }
}
