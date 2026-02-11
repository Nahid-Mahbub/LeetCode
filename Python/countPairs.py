class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:
        counter = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(nums[i] == nums[j] and i != j):
                    if((i*j) % k == 0):
                        print(i, j)
                        counter += 1
        return counter // 2
solution = Solution()
nums = [3,1,2,2,2,1,3]
k = 2
result = solution.countPairs(nums, k)
print(result)