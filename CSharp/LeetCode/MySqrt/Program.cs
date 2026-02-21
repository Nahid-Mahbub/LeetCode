using System.Linq;
using System.Diagnostics.Metrics;

class Program
{
    static void Main()
    {
        int x = 4;
        Console.WriteLine(MySqrt(x));
    }

    public static int MySqrt(int x)
    {
        return (int)Math.Sqrt(x);
    }

}
