class Solution:
    def triangleType(self, nums: list[int]) -> str:
        nums.sort()
        print(nums)
        if (nums[0] + nums[1] <= nums[2]):
            return "none"
        if (nums[0] == nums[1] and nums[1] == nums[2]):
            return "equilateral"
        elif (nums[0] == nums[1] and nums[1] < nums[2] or nums[1] == nums[2] and nums[0] < nums[1]):
            return "isosceles"
        else:
            return "scalene"
        
solution = Solution()
nums = [5,4,3]
result = solution.triangleType(nums)
print(result)