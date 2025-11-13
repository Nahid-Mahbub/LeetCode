class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome = []
        for i in range(len(s)):
            asciiValue = ord(s[i])
            if(asciiValue <= 90 and 65 <= asciiValue):
                palindrome.append(chr(asciiValue + 32))
            elif(asciiValue <= 122 and 97 <= asciiValue):
                palindrome.append(s[i])
            elif(asciiValue <= 57 and 48 <= asciiValue):
                palindrome.append(s[i])
        print(palindrome, palindrome[::-1])
        if(palindrome == palindrome[::-1]):
            return True
        return False

solution = Solution()
s = "0P"
result = solution.isPalindrome(s)
print(result)