class Solution:
    def maxDistinct(self, s: str) -> int:
        return len(set(s))
solution = Solution()
s = "abcd"
result = solution.maxDistinct(s)
print(result)