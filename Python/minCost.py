class Solution:
    def minCost(self, n: int) -> int:
        return (n * (n-1) // 2)
    
solution = Solution()
n = 4
result = solution.minCost(n)
print(result)