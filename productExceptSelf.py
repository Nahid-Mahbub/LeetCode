class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        length = len(nums)
        prefix = [0] * length
        suffix = [0] * length
        result = [0] * length
        prefix[0] = 1
        suffix[length-1] = 1
        for i in range(1, length):
            prefix[i] = nums[i-1] * prefix[i-1]
            print(nums[i-1], prefix[i-1])
        print()
        for i in range(length-2, -1, -1):
            suffix[i] = nums[i+1] * suffix[i+1]
            print(nums[i+1], suffix[i+1])
        print()
        for i in range(length):
            result[i] = prefix[i] * suffix[i]
            print(prefix[i], suffix[i])
        print(prefix, suffix)
        return result
solution = Solution()
nums = [1,2,3,4]
result = solution.productExceptSelf(nums)
print(result)