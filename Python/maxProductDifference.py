class Solution:
    def maxProductDifference(self, nums: list[int]) -> int:

        nums.sort()
        return (nums[-1] * nums[-2]) - (nums[0] * nums[1])
    
solution = Solution()
nums = [5,6,2,7,4]
result = solution.maxProductDifference(nums)
print(result)