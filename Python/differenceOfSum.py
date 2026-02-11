class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        digits = [int(d) for num in nums for d in str(num)]
        return abs(sum(nums) - sum(digits))
    
solution = Solution()
nums = [1,15,6,3]
result = solution.differenceOfSum(nums)
print(result)