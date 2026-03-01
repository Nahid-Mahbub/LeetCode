using System;

class Program
{
    static void Main()
    {
        int[] nums = [0, 1, 0, 3, 12];
        MoveZeroes(nums);
        //Console.WriteLine(MoveZeroes(nums));
    }

    public static void MoveZeroes(int[] nums)
    {
        int index = 0;
        foreach (int x in nums)
        {
            if(x != 0)
            {
                nums[index] = x;
                index++;
            }
        }

        while (index < nums.Length)
        {
            nums[index] = 0;
            index++;
        }
        
        foreach(int x in nums)
            Console.Write($"{x} ");
    }
}
