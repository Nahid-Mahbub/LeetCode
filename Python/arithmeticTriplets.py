class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        counter = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if(nums[j] - nums[i] == diff):
                    for k in range(j+1, len(nums)):
                        if(nums[k] - nums[j] == diff):
                            counter += 1
        return counter

solution = Solution()
nums = [0,1,4,6,7,10]
diff = 3
result = solution.arithmeticTriplets(nums, diff)
print(result)
