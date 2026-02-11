class Solution:
    def minPartitions(self, n: str) -> int:
        # return max(map(int, n))
        maxNum = 0
        for i in range(len(n)):
            if(int(n[i]) > maxNum):
                maxNum = int(n[i])
        return maxNum
    
solution = Solution()
n = "32"
result = solution.minPartitions(n)
print(result)