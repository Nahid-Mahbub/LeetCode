class Solution:
    def distinctDifferenceArray(self, nums: list[int]) -> list[int]:
        output = []
        for i in range(len(nums)):
            # print(len(set(nums[:i+1])), len(set(nums[i:])))
            output.append(len(set(nums[:i+1])) - len(set(nums[i+1:])))
        return output
solution = Solution()
nums = [3,2,3,4,2]
result = solution.distinctDifferenceArray(nums)
print(result)