class Solution:
    def search(self, nums: list[int], target: int) -> int:
        for i in range(len(nums)):
            if(nums[i] == target):
                return i
        return -1
    # Oneline -> return nums.index(target) if(target in nums) else -1

solution = Solution()
nums = [-1,0,3,5,9,12]
target = 9
result = solution.search(nums, target)
print(result)