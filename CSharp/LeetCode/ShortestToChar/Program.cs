using System;

class Program
{
    static void Main()
    {
        string s = "loveleetcode";
        char c = 'e';
        //Console.WriteLine(Intersection(nums1, nums2));
        foreach (int x in ShortestToChar(s, c))
        {
            Console.WriteLine(x);
        }
    }

    public static int[] ShortestToChar(string s, char c)
    {
        List<int> charIndex = new List<int>();
        List<int> answer = new List<int>();

        for (int i = 0; i < s.Length; i++)
        {
            if (s[i] == c)
            {
                charIndex.Add(i);
            }
        }

        for (int i = 0; i < s.Length; i++)
        {
            int val = int.MaxValue;
            foreach (int count in charIndex)
            {
                int distance = Math.Abs(count - i);
                
                if(distance < val)
                {
                    val = distance;
                }
            }
            answer.Add(val);
        }

        return answer.ToArray();
    }
}
