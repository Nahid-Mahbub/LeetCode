class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []

        # Base case
        if(len(nums) == 1):
            return [nums[:]]
        
        for i in range(len(nums)):
            pop_value = nums.pop(0)
            recursions = self.permute(nums)
            for recursion in recursions:
                recursion.append(pop_value)
            result.extend(recursions)
            nums.append(pop_value)

        return result
    
solution = Solution()
nums = [1,2,3]
result = solution.permute(nums)
print(result)