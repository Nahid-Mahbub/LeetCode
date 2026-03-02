using System;

class Program
{
    static void Main()
    {
        int[] nums = [1, 2, 3, 2];
        Console.WriteLine(SumOfUnique(nums));
    }

    public static int SumOfUnique(int[] nums)
    {
        HashSet<int> setNums = new HashSet<int>(nums);
        
        if(setNums.Count == nums.Length)
        {
            return nums.Sum(x => x);
        }

        nums.Sort();
        HashSet<int> array = new HashSet<int>();
        int temp = nums[0];

        for (int i = 1; i < nums.Length; i++)
        {
            if (temp == nums[i])
            {
                array.Add(nums[i]);
            }
            else
            {
                temp = nums[i];
            }
        }

        foreach (int i in array)
        {
            setNums.Remove(i);
        }

        return setNums.Sum();

    }
}
