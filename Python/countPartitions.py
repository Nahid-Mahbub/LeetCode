class Solution:
    def countPartitions(self, nums: list[int]) -> int:
        # counter = 0
        # for i in range(len(nums)- 1):
        #     if(((sum(nums[:i+1])) - (sum(nums[i+1:]))) % 2 == 0):
        #         counter += 1
        # return counter
        allSum = sum(nums)
        if(allSum % 2 == 0):
            return len(nums) - 1
        else:
            return 0
        
solution = Solution()
nums = [10,10,3,7,6]
result = solution.countPartitions(nums)
print(result)