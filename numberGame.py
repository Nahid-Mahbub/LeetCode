class Solution:
    def numberGame(self, nums: list[int]) -> list[int]:
        nums.sort()
        for i in range(0, len(nums)-1, 2):
            nums[i], nums[i+1] = nums[i+1], nums[i]
        return nums
    
solution = Solution()
nums = [5,4,2,3]
result = solution.numberGame(nums)
print(result)