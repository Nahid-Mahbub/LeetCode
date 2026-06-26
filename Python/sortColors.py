class Solution:
    def sortColors(self, nums: list[int]) -> None:
        n = len(nums)
        for i in range(n):
            for j in range(n - i - 1):
                if (nums[j] > nums[j+1]):
                    nums[j], nums[j+1] = nums[j+1], nums[j]

solution = Solution()
nums = [2,0,2,1,1,0]
result = solution.sortColors(nums)
print(nums)