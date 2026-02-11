class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        numMax =  max(nums)
        output = 0
        for i in range(k):
            output += numMax + i
        return output
    
solution = Solution()
nums = [5, 5, 5]
k = 2
result = solution.maximizeSum(nums, k)
print(result)