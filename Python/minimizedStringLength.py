class Solution:
    def minimizedStringLength(self, s: str) -> int:
        return len(set(s))

solution = Solution()
s = "aaabc"
result = solution.minimizedStringLength(s)
print(result)