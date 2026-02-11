class Solution:
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        
        new_arr = []
        for i in range (0,len(nums),2):
            for j in range (nums[i]):
                new_arr.append(nums[i+1])
        return new_arr

solution = Solution()
nums = [1,2,3,4]
result = solution.decompressRLElist(nums)
print(result)