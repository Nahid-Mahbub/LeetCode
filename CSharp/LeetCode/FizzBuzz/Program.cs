using System;

class Program
{
    static void Main()
    {
        int num = 3;
        var result = FizzBuzz(num);

        foreach (var item in result)
        {
            Console.WriteLine(item);
        }
    }

    public static IList<string> FizzBuzz(int n)
    {
        IList<string> list = new List<string>();

        for (int i = 1; i <= n; i++)
        {
            if(i % 3 == 0 & i % 5 == 0)
            {
                list.Add("FizzBuzz");
            }
            else if(i % 3 == 0)
            {
                list.Add("Fizz");
            }
            else if( i % 5 == 0)
            {
                list.Add("Buzz");
            }
            else
            {
                list.Add(i.ToString());
            }
        }
        return list;
    }
}
