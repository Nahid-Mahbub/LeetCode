class Solution:
    def scoreOfString(self, s: str) -> int:
        value = 0
        initial = ord(s[0])
        for i in range(1, len(s)):
            value += abs(initial - ord(s[i]))
            initial = ord(s[i])
        return value
solution = Solution()
s = "hello"
result = solution.scoreOfString(s)
print(result)