class Solution:
    def sumIndicesWithKSetBits(self, nums: list[int], k: int) -> int:
        numSum = 0
        for i in range(len(nums)):
            bin_nums = bin(i)
            counter = 0
            
            for bin_num in bin_nums:
                print(bin_num)
                if(bin_num == "1"):
                    counter += 1
            print()
            print("Counter :", counter)
            if (counter == k):
                numSum += nums[i]
        return numSum
solution = Solution()
nums = [5,10,1,5,2]
k = 1
result = solution.sumIndicesWithKSetBits(nums, k)
print(result)