using System.Linq;
using System.Diagnostics.Metrics;

class Program
{
    static void Main()
    {
        int[] digits = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0];
        //Console.WriteLine(PlusOne(digits));
        foreach (int digit in PlusOne(digits))
        {
            Console.Write(digit);
        }
    }

    public static int[] PlusOne(int[] digits)
    {
        for (int i = digits.Length - 1; i >= 0; i--)
        {
            if (digits[i] < 9)
            {
                digits[i]++;
                return digits;
            }
            digits[i] = 0;
        }

        int[] output = new int[digits.Length + 1];
        output[0] = 1;
        return output;
    }
}
