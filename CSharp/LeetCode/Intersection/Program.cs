using System;

class Program
{
    static void Main()
    {
        int[] nums1 = [4, 9, 5];
        int[] nums2 = [9, 4, 9, 8, 4];
        //Console.WriteLine(Intersection(nums1, nums2));
        foreach (int x in Intersection(nums1, nums2))
        {
            Console.WriteLine(x);
        }
    }

    public static int[] Intersection(int[] nums1, int[] nums2)
    {
        return nums1.Intersect(nums2).ToArray();
    }
}
