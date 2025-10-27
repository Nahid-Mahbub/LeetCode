class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums.sort()
        counter = 0
        res = 0
        if(len(nums) == 0):
            return 0
        for i in range(len(nums)-1):
            index = 0
            if(nums[i]+1 == (nums[i+1])):
                counter += 1
                if(res < counter):
                    res = counter
            elif(nums[i] == nums[i+1]):
                continue
            else:
                counter = 0
        return res+1
        
solution = Solution()
nums = [1,0,1,2]
result = solution.longestConsecutive(nums)
print(result)