class Solution:
    def triangularSum(self, nums: list[int]) -> int:
        
        if (len(nums) == 1):
            return nums[0]
        result = []
        for i in range(1, len(nums)):
            result.append((nums[i-1] + nums[i]) % 10 )
        while len(result) > 1:
            print(result)
            temp = []
            for i in range(1, len(result)):
                temp.append((result[i-1] + result[i]) % 10)
            result = temp.copy()
        return result[0]
solution = Solution()
nums = [1, 2]
result = solution.triangularSum(nums)
print(result)