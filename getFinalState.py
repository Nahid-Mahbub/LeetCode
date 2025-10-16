class Solution:
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        for i in range(k):
            minValue = min(nums)
            minIndex = nums.index(minValue)
            nums[minIndex] = nums[minIndex] * multiplier
            print(minValue, minIndex, nums[minIndex])
        return nums
        
solution = Solution()
nums = [1,2]
k = 3
multiplier = 4
result = solution.getFinalState(nums, k, multiplier)
print(result)
