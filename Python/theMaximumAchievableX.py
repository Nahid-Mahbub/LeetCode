class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + (t * 2)
solution = Solution()
num = 4
t = 1
result = solution.theMaximumAchievableX(num, t)
print(result)