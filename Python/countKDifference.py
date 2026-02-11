class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        counter = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if(abs(nums[i] - nums[j]) == k):
                    counter += 1
        return counter

solution = Solution()
nums = [1,2,2,1]
k = 1
result = solution.countKDifference(nums, k)
print(result)