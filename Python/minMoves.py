class Solution:
    def minMoves(self, nums: list[int]) -> int:
        length = len(nums) - 1
        nums.sort()
        counter = 0
        for num in nums:
            counter += nums[length] - num
        return counter
solution = Solution()
nums = [2,1,3]
result = solution.minMoves(nums)
print(result)