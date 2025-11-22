class Solution:
    def countDigits(self, num: int) -> int:
        counter = 0
        strNum = str(num)
        for i in range(len(strNum)):
            if(num % int(strNum[i]) == 0):
                counter += 1
        return counter

solution = Solution()
num = 7
result = solution.countDigits(num)
print(result)