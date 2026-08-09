class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        return min(n*n, maxWeight // w)
    
solution = Solution()
n = 3
w = 5
maxWeight = 20
result = solution.maxContainers(n, w, maxWeight)
print(result)