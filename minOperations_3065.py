class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        counter = 0
        for num in nums:
            if (num < k):
                counter += 1
        return counter

solution = Solution()
nums = [2,11,10,1,3]
k = 10
result = solution.minOperations(nums, k)
print(result)