using System;

class Program
{
    static void Main()
    {
        int[] nums = [3, 2, 1];

        Console.WriteLine(ThirdMax(nums));
    }

    public static int ThirdMax(int[] nums)
    {
        HashSet<int> set = new HashSet<int>(nums);
        int[] newNums = set.ToArray();

        Array.Sort(newNums);
        Array.Reverse(newNums);

        return newNums.Length >= 3 ? newNums[2] : newNums[0];
    }
}
