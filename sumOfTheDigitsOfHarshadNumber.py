class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        strX = str(x)
        counter = 0
        for num in strX:
            counter += int(num)
        if(x % counter == 0):
            return counter
        else:
            return -1

solution = Solution()
x = 18
result = solution.sumOfTheDigitsOfHarshadNumber(x)
print(result)