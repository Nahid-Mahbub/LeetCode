class Solution:
    def maxKDistinct(self, nums: list[int], k: int) -> list[int]:
        numsNew = sorted(list(set(nums)), reverse = True)
        return numsNew[:k]
    
solution = Solution()
nums = [84,93,100,77,93]
k = 3
result = solution.maxKDistinct(nums, k)
print(result)