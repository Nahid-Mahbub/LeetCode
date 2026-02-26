using System;

class Program
{
    static void Main()
    {
        int num = 38;
        Console.WriteLine(AddDigits(num));
    }

    public static int AddDigits(int num)
    {
        while(true)
        {
            string numS = num.ToString();
            if (numS.Length < 2)
            {
                return int.Parse(numS.ToString());
            }

            int temp = 0;
            foreach (char c in numS)
            {
                temp += c - '0';
            }
            num = temp;
        }
    }
}
