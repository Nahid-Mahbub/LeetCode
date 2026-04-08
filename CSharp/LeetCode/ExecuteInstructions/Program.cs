using System;
using System.Data;
using System.Diagnostics.Metrics;

class Program
{
    static void Main()
    {
        int n = 3;
        int[] startPos = [0, 1];
        string s = "RRDDLU";
         foreach (int i in ExecuteInstructions(n, startPos, s))
        {
            Console.WriteLine(i);
        }
    }

    public static int[] ExecuteInstructions(int n, int[] startPos, string s)
    {
        List<int> result = new List<int>();

        for (int i = 0; i < s.Length; i++)
        {
            int x = startPos[0];
            int y = startPos[1];
            
            int counter = 0;

            for (int j = i; j < s.Length; j++)
            {
                if (s[j] == 'R')
                    y += 1;
                else if (s[j] == 'L')
                    y -= 1;
                else if (s[j] == 'U')
                    x -= 1;
                else if (s[j] == 'D')
                    x += 1;

                if (x < 0 || x >= n || y < 0 || y >= n)
                    break;

                counter++;
            }

            result.Add(counter);
        }

        return result.ToArray();
    }
}
