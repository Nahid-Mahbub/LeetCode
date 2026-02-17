using System;

class Program
{
    static void Main()
    {
        string s = "()[]{}";
        Console.WriteLine(IsValid(s));
    }

    public static bool IsValid(string s)
    {
        Dictionary<char, char> myDic = new Dictionary<char, char>();
        Stack<char> stack = new Stack<char>();
        myDic[')'] = '(';
        myDic['}'] = '{';
        myDic[']'] = '[';

        foreach (char c in s)
        {
            if (myDic.ContainsKey(c))
            {
                if(stack.Count == 0 || stack.Pop() != myDic[c])
                {
                    return false;
                }
            }
            else
            {
                stack.Push(c);
            }
        }
        return stack.Count == 0;
    }
}
