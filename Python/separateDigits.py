class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        output = []
        for num in nums:
            if(len(str(num)) > 1):
                output += [int(d) for d in str(num)]
            else:
                output.append(num)
        return output
    
solution = Solution()
nums = [13,25,83,77]
result = solution.separateDigits(nums)
print(result)