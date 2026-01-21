class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        output = []
        freqDic = {}
        for num in nums:
            freqDic[num] = freqDic.get(num, 0) + 1
        print(max(freqDic.values()))
        for i in range(max(freqDic.values())):
            row = []
            for num in set(nums):
                if(freqDic[num] != 0):
                    row.append(num)
                    freqDic[num] =  freqDic[num] - 1
            output.append(row)
        return output
    
solution = Solution()
nums = [1,3,4,1,2,3,1]
result = solution .findMatrix(nums)
print(result)