class Solution:
    def maximum69Number (self, num: int) -> int:
        strNum = list(str(num))
        print(strNum)
        if ('6' not in strNum):
            return num
        else:
            index = strNum.index('6')
            strNum[index] = '9'
            return int("".join(strNum))
        
solution = Solution()
num = 9669
result = solution.maximum69Number(num)
print(result)