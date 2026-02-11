class Solution:
    def conversion(self, num, base):
        if(num == 0):
            return "0"
        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = ""
        while num > 0:
            result = digits[num % base] + result
            num //= base
        return result
    def sumBase(self, n: int, k: int) -> int:
        output = 0
        convertedNum = self.conversion(n, k)
        for num in convertedNum:
            output += int(num)
        return output
solution = Solution()
n = 34
k = 6
result = solution.sumBase(n, k)
print(result)