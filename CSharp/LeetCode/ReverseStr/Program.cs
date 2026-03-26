using System;
using System.Globalization;
using System.Runtime.CompilerServices;
using System.Text;

 class Program
 {
    static void Main()
    {
        string s = "abcdefg";
        int k = 2;
        Console.WriteLine(ReverseStr(s, k));
    }

    public static string ReverseStr(string s, int k)
    {
        char[] array = s.ToCharArray();
        for (int i = 0; i < s.Length; i += 2 * k)
        {
            int left = i;
            int right = Math.Min(i + k - 1, s.Length - 1);

            while(left < right)
            {
                char temp = array[left];
                array[left] = array[right];
                array[right] = temp;

                left++;
                right--;
            }
        }

        return new string(array);
    }
}
