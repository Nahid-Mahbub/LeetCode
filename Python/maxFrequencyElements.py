class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        counter = 0
        index_val = [0] * (max(nums)+1)
        for num in nums:
            index_val[num] += 1
        val = max(index_val)
        for num in index_val:
            if(val == num):
                counter += val
        return counter
    
solution = Solution()
nums = [1,2,2,3,1,4]
result = solution.maxFrequencyElements(nums)
print(result)