class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        import itertools
        subset = []
        for i in range(len(nums)+1):
             subset.extend([list(comb) for comb in itertools.combinations(nums, i)])
        return subset
solution = Solution()
nums = [1,2,3]
result = solution.subsets(nums)
print(result)