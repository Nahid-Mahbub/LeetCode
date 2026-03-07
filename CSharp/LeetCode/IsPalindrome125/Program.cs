using System;
using System.Text;

class Program
{
    static void Main()
    {
        string s = "0P";
        Console.WriteLine(IsPalindrome(s));
    }

    public static bool IsPalindrome(string s)
    {
        StringBuilder newString = new StringBuilder();
        foreach (char c in s)
        {
            if (char.IsLetterOrDigit(c))
            {
                newString.Append(char.ToLower(c));
            }
            else
                continue;
        }



        int left = 0;
        int right = newString.Length - 1;
        while (left < right)
        {
            if(newString[left] != newString[right])
                return false;
            left++;
            right--;
        }
        return true;
    }
}
