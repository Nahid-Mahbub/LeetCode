using System;
using System.Data;

class Program
{
    static void Main()
    {
        int numBottles = 65;
        int numExchange = 3;
        Console.WriteLine(NumWaterBottles(numBottles, numExchange));
    }

    public static int NumWaterBottles(int numBottles, int numExchange)
    {
        int result = numBottles;
        int remain = 0;
        while (numBottles >= numExchange)
        {
            result += numBottles / numExchange;
            remain = numBottles % numExchange;

            numBottles = (numBottles / numExchange) + remain;
        }
        return result;
    }
}
