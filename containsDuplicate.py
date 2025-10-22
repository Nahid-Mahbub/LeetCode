class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        setNums = set(nums)
        if(len(setNums) == len(nums)):
            return False
        return True

solution = Solution()
nums = [1,2,3,1]
result = solution.containsDuplicate(nums)
print(result)