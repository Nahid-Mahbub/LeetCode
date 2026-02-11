class Solution:
    def addDigits(self, num: int) -> int:        
        # strNum = str(num)
        # print(strNum, type(strNum), strNum[0])
        # while(len(strNum) > 1):
        #     sumNum = 0
        #     for num in strNum:
        #         sumNum += int(num)
        #     strNum = str(sumNum)
        # return int(strNum)
        if num == 0:
            return 0
        elif num % 9 == 0:
            return 9
        else:
            return (num % 9)
    
solution = Solution()
num = 38
result = solution.addDigits(num)
print(result)