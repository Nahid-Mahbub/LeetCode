class Solution:
    def isArraySpecial(self, nums: list[int]) -> bool:
        if(len(nums) < 2):
            return True
        
        for i in range(len(nums)-1):
            if((nums[i]%2 == 0) == (nums[i+1]%2 == 0)):
                return False
        return True

solution = Solution()
nums = [2,1,4]
result = solution.isArraySpecial(nums)
print(result)