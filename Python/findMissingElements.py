class Solution:
    def findMissingElements(self, nums: list[int]) -> list[int]:
        output = []
        setNums = set(nums)
        minNum = min(setNums)
        maxNum = max(setNums)

        for i in range(minNum, maxNum):
            if(i not in setNums):
                output.append(i)
        return output

solution = Solution()
nums = [1,4,2,5]
result = solution.findMissingElements(nums)
print(result)