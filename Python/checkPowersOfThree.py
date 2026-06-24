class Solution:
    def convert_base(self, num, base):
        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = ""
        if num == 0:
            return "0"
        while num > 0:
            result = digits[num % base] + result
            num //= base
        return result
        
    def checkPowersOfThree(self, n: int) -> bool:
        check = self.convert_base(n, 3)
        if("2" in check):
            return False
        return True

solution = Solution()
n = 12
result = solution.checkPowersOfThree(n)
print(result)