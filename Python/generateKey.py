from unittest import result
class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        result = ""
        str_num1 = str(num1)
        str_num2 = str(num2)
        str_num3 = str(num3)
        if len(str_num1) < 4:
            for i in range(4 - len(str(num1))):
                str_num1 = "0" + str_num1
        if len(str_num2) < 4:
            for i in range(4 - len(str(num2))):
                str_num2 = "0" + str_num2
        if len(str_num3) < 4:
            for i in range(4 - len(str(num3))):
                str_num3 = "0" + str_num3
        print(str_num1, str_num2, str_num3)
        for i in range(4):
            result += min(str_num1[i], str_num2[i], str_num3[i])
        return int(result)

solution = Solution()
num1 = 1
num2 = 10 
num3 = 1000
result = solution.generateKey(num1, num2, num3)
print(result)