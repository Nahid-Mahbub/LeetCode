class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        nums = nums + nums[::-1]
        return nums
      
solution = Solution()
nums = [1,2,3]
result = solution.concatWithReverse(nums)
print(result)
