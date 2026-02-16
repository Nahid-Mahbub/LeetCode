using System;

class Program
{
    static void Main()
    {
        int x = 121;
        Console.WriteLine(IsPalindrome(x));
    }

    public static bool IsPalindrome(int x)
    {
        string original = x.ToString();

        char[] chars = original.ToCharArray();
        Array.Reverse(chars);

        string reversed = new string(chars);

        if (original == reversed)
        {
            return true;
        }
        else
        {
            return false;
        }

        // return original == reversed

    }
}
