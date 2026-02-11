class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        joinNums = ""
        output = []
        for num in nums:
            joinNums += str(num) 
            if (int(joinNums, 2) % 5 == 0): # To convert bin -> dec we use int(str(num), base)
                output.append(True)
            else:
                output.append(False)
        return output
solution = Solution()
nums = [0,1,1]
result = solution.prefixesDivBy5(nums)
print(result)