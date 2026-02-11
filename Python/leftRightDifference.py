class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        length = len(nums)
        ans = [0]* length
        counter = 0
        for i in range(length):
            ans[i] = counter
            counter += nums[i]
        counter = 0

        for j in range(length-1, -1, -1):
            ans[j] = abs(ans[j]-counter)
            counter += nums[j]        
        return ans

solution = Solution()
nums = [10,4,8,3]
result = solution.leftRightDifference(nums)
print(result)