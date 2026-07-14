class Solution:
    def countDistinctIntegers(self, nums: list[int]) -> int:
        result = set(nums.copy())
        for num in nums:
            result.add(int(str(num)[::-1]))
        return len(result)
        
solution = Solution()
nums = [1,13,10,12,31]
result = solution.countDistinctIntegers(nums)
print(result)
