using System;
using System.Data;
using System.Diagnostics.Metrics;

class Program
{
    static void Main()
    {
        int low = 1;
        int high = 100;
        Console.WriteLine(CountSymmetricIntegers(low, high));
    }

    public static int CountSymmetricIntegers(int low, int high)
    {
        int counter = 0;
        for (int i = low; i <= high; i++)
        {
            string num = i.ToString();
            if (num.Length %  2 == 0)
            {
                int first = 0;
                int second = 0;

                for (int j = 0; j < num.Length; j++)
                {
                    if (j < num.Length / 2)
                    {
                        first += int.Parse(num[j].ToString());
                    }
                    else
                    {
                        second += int.Parse(num[j].ToString());
                    }
                }

                if (first == second)
                    counter++;
            }
            
        }

        return counter;
    }
}
