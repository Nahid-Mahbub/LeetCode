using System;

class Program
{
    static void Main()
    {
        string[] words = ["Hello", "Alaska", "Dad", "Peace"];
        //Console.WriteLine(Intersection(nums1, nums2));
        foreach (string x in FindWords(words))
        {
            Console.WriteLine(x);
        }
    }

    public static string[] FindWords(string[] words)
    {
        char[] first = { 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p' };
        char[] second = { 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l' };
        char[] third = { 'z', 'x', 'c', 'v', 'b', 'n', 'm' };

        List<string> listWords = new List<string>(words);
        List<string> answer = new List<string>(words);
        foreach (string word in listWords)
        {
            string newString = word.ToLower();
            if (first.Contains(newString[0]))
            {
                foreach (char c in newString)
                {
                    if (!(first.Contains(c)))
                    {
                        answer.Remove(word);
                        break;
                    }
                }
            }

            else if (second.Contains(newString[0]))
            {
                foreach (char c in newString)
                {
                    if (!(second.Contains(c)))
                    {
                        answer.Remove(word);
                        break;
                    }
                }
            }

            else
            {
                foreach (char c in newString)
                {
                    if (!(third.Contains(c)))
                    {
                        answer.Remove(word);
                        break;
                    }
                }
            }
        }

        return answer.ToArray();
    }
}
