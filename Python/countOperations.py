class Solution:
    def subtract(self, arg1: int, arg2: int):
        return arg1 - arg2    
    def countOperations(self, num1: int, num2: int) -> int:
        counter = 0
        while (num1 != 0 and num2 != 0):
            counter += 1
            if(num2 > num1):
                num2 = self.subtract(num2, num1)
            else:
                num1 = self.subtract(num1, num2)
        return counter
solution = Solution()
num1 = 2
num2 = 3
result = solution.countOperations(num1, num2)
print(result)