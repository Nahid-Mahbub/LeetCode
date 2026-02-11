class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        nums.sort()
        lenght = len(nums)
        minSum = 1
        maxSum = 1
        for i in range(1, 4):
            maxSum *= nums[lenght - i]
            if(i == 3):
                minSum *= nums[lenght - 1]
                return minSum if minSum > maxSum else maxSum
            minSum *= nums[i-1]
solution = Solution()
nums = [-100,-98,-1,2,3,4]
result = solution.maximumProduct(nums)
print(result)