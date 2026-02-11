class Solution:
    def minOperations(self, nums: list[int]) -> int:
        counter = 0
        for i in range(1, len(nums)):
            if(nums[i-1] >= nums[i]):
                counter += (nums[i - 1] + 1) - nums[i]
                nums[i] = nums[i - 1] + 1
        return counter
solution = Solution()
nums = [1,1,1]
result = solution.minOperations(nums)
print(result)