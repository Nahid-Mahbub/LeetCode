class Solution:
    def mirrorDistance(self, n: int) -> int:
        return abs(n - int(str(n)[::-1]))
    
solution = Solution()
n = 25
result = solution.mirrorDistance(n)
print(result)