class Solution:
    def findGCD(self, nums: list[int]) -> int:
        minNums = min(nums)
        maxNums = max(nums)
        while minNums != 0:
            maxNums, minNums = minNums, maxNums % minNums
        return maxNums
    
solution = Solution()
nums = [2,5,6,9,10]
result = solution.findGCD(nums)
print(result)