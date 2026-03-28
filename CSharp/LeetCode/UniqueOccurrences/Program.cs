using System;
using System.Data;

class Program
{
    static void Main()
    {
        int[] arr = [1, 2, 2, 1, 1, 3];
        Console.WriteLine(UniqueOccurrences(arr));
    }

    public static bool UniqueOccurrences(int[] arr)
    {
        Dictionary<int, int> occurrence =  new Dictionary<int, int>();
        HashSet<int> visited = new HashSet<int>();

        foreach (int i in arr)
        {
            if (occurrence.ContainsKey(i))
            {
                occurrence[i]++;
            }
            else
            {
                occurrence.Add(i, 1);
            }
        }

        foreach (var pair in occurrence)
        {
            visited.Add(pair.Value);
        }

        return visited.Count() == occurrence.Count();
    }
}
