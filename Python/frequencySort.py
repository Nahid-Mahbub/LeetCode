class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        myDic = {}
        output = []

        for num in nums:
            if num in myDic:
                myDic[num] += 1
            else:
                myDic[num] = 1
        while myDic:
            temp = 101
            myDic_Value = None
            for key, value in myDic.items():
                if(temp > value):
                    temp = value
                    myDic_Value = key
                elif(temp == value):
                    if(myDic_Value < key):
                        myDic_Value = key
            myDic.pop(myDic_Value)
            output += ([myDic_Value] * temp)
        return output
    

solution = Solution()
nums = [1,1,2,2,2,3]
result = solution.frequencySort(nums)
print(result)