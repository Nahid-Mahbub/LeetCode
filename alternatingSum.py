class Solution:
    def alternatingSum(self, nums: list[int]) -> int:
        output = 0
        for i in range(len(nums)):
            if(i % 2 == 0):
                output += nums[i]
            else:
                output -= nums[i]
        return output
    
solution = Solution()
nums = [1,3,5,7]
result = solution.alternatingSum(nums)
print(result)