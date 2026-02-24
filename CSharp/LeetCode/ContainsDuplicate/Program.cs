using System;

class Program
{
    static void Main()
    {
        int[] nums = [1, 2, 3, 1];
        Console.WriteLine(ContainsDuplicate(nums));
    }

    public static bool ContainsDuplicate(int[] nums)
    {
        HashSet<int> set = new HashSet<int>();
        foreach (int x in nums)
        {
            set.Add(x);
        }
        return set.Count() != nums.Length;
    }
}
