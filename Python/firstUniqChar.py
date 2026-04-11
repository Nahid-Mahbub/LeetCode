class Solution:
    def firstUniqChar(self, s: str) -> int:
        setString = dict()
        for char in s:
            setString[char] = setString.get(char, 0) + 1
        print(setString)
        
        for i in range(len(s)):
            if (setString.get(s[i]) == 1):
                return i
        return -1

solution = Solution()
s = "leetcode"
result = solution.firstUniqChar(s)
print(result)