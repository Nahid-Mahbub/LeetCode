class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        counter = 0
        # length = len(nums)
        # for binary in range(1 << length): #(1 << length) -> 1 * 2^length
        #     sum = 0
        #     for i in range(length):
        #         if(binary & (1 << i)):
        #             sum ^= nums[i]
        #     counter += sum
        # return counter
        
        # Final_ans = (Bitwise OR of all nums) * 2^(n-1)
        for num in nums:
            counter |= num
        return counter * (1 << len(nums)-1)
solution = Solution()
nums = [5,1,6]
result = solution.subsetXORSum(nums)
print(result)