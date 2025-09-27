class Solution:
    def canBeIncreasing(self, nums: list[int]) -> bool:
        nums_copy = nums.copy()

        for i in range(len(nums_copy)):
            nums_copy.pop(i)
            if (len(nums_copy) == 1):
                return True
            for j in range(len(nums_copy) - 1):
                if(nums_copy[j] < nums_copy[j+1]):
                    # print(nums_copy, j)
                    if(j+2 == len(nums_copy)):
                        # print("Done")
                        return True
                else:
                    break

            nums_copy = nums.copy()
        return False
            

solution = Solution()
nums = [1,1]
result = solution.canBeIncreasing(nums)
print(result)