class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        counter = 0
        nums_str = [str(i) for i in nums]
        for num in nums_str:
            if (len(num) % 2 == 0):
                counter += 1
        return counter
    
solution = Solution()
nums = [12,345,2,6,7896]
result = solution.findNumbers(nums)
print(result)