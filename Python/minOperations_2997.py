class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        xor_sum = 0
        for num in nums:
            xor_sum ^= num

        return (xor_sum ^ k).bit_count() #bit_count() counts the number of 1's in the binary representation of the number


solution = Solution()
nums = [2,1,3,4]
k = 1
result = solution.minOperations(nums, k)
print(result)