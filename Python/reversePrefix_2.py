class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
       return s[:k][::-1] + s[k::]

solution = Solution()
s = "abcd"
k = 2
result = solution.reversePrefix(s, k)
print(result)