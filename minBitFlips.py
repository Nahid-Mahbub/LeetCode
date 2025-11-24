class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return bin(start ^ goal).count("1")

solution = Solution()
start = 10
goal = 7
result = solution.minBitFlips(start, goal)
print(result)