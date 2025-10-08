class Solution:
    def sumOfSquares(self, nums: list[int]) -> int:
        length = len(nums)
        counter = 0
        for i in range(len(nums)):
            if(length % (i+1) == 0):
                counter += nums[i]*nums[i]
        return counter

solution = Solution()
nums = [1,2,3,4]
result = solution.sumOfSquares(nums)
print(result)