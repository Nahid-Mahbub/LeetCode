class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        
        less = []
        greater = []
        equal = []
        for i in range(len(nums)):
            if (pivot > nums[i]):
                less.append(nums[i])
            elif (pivot < nums[i]):
                greater.append(nums[i])
            else:
                equal.append(nums[i])
        return less+equal+greater
        


solution = Solution()
nums = [9,12,5,10,14,3,10]
pivot = 10
result = solution.pivotArray(nums, pivot)
print(result)