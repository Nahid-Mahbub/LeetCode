using System;

class Program
{
    static void Main()
    {
        char[] letters = ['c','f','j'];
        char target = 'c';
        Console.WriteLine(NextGreatestLetter(letters, target));
    }

    public static char NextGreatestLetter(char[] letters, char target)
    {
        foreach (char c in letters)
        {    
            if (target < c)
                return c;
        }
        return letters[0];
    }
}
