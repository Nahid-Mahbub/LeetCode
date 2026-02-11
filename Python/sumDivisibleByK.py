
class Solution:
    def sumDivisibleByK(self, nums: list[int], k: int) -> int:
        from collections import Counter
        sumNums = 0
        # setNums = set(nums)
        # for num in setNums:
        #     counter = 0
        #     for listNum in nums:
        #         if(num == listNum):
        #             counter += 1
        #     if(counter % k == 0):
        #         sumNums += (counter * num)
        # return sumNums
        freq = Counter(nums)
        for num, count in freq.items():
            if(count % k == 0):
                sumNums += (num * count)
        return sumNums
        
solution = Solution()
nums = [4,4,4,1,2,3]
k = 3
result = solution.sumDivisibleByK(nums, k)
print(result)