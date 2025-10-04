class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        new_list = [nums[0]]
        for i in range(1, len(nums)):
            new_list.append(nums[i] + new_list[i-1])
        return new_list
solution = Solution()
nums = [1,2,3,4]
result = solution.runningSum(nums)
print(result)