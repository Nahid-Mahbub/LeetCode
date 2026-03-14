class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        newString = []
        for x in s:
            if (x.isalpha()):
                newString.append(x)
        right = len(newString) - 1
        s = list(s)
        print(newString)
        for left in range(len(s)):
            if (s[left].isalpha()):
                s[left] = newString[right]
                right -= 1
        return "".join(s)
    
solution = Solution()
s = "ab-cd"
result = solution.reverseOnlyLetters(s)
print(result)