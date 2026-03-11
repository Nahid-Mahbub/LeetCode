using System;

class Program
{
    static void Main()
    {
        int[] nums = [4, 3, 2, 1];
        //Console.WriteLine(Intersection(nums1, nums2));
        foreach (int x in TransformArray(nums))
        {
            Console.WriteLine(x);
        }
    }

    public static int[] TransformArray(int[] nums)
    {
        List<int> answer = new List<int>(nums);

        for (int i = 0; i < nums.Length; i++)
        {
            if (answer[i] % 2 == 0)
            {
                answer[i] = 0;
            }
            else
            {
                answer[i] = 1;
            }
        }
        answer.Sort();
        return answer.ToArray();
    }
}
