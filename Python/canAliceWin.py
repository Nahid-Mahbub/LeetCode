class Solution:
    def canAliceWin(self, nums: list[int]) -> bool:
        lessCounter = 0
        greaterCounter = 0
        for num in nums:
            if (num < 10):
                lessCounter += num
            else:
                greaterCounter += num
        return lessCounter != greaterCounter

solution = Solution()
nums = [1,2,3,4,10]
result = solution.canAliceWin(nums)
print(result)