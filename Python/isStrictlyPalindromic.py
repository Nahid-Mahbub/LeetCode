class Solution:
    def decimal_to_base(self, n, base):
        digits = "0123456789ABCDEF"
        if n == 0:
            return "0"

        result = ""
        while n > 0:
            result = digits[n % base] + result
            n //= base

        return result

    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2, n - 1):
            palindromic = str(self.decimal_to_base(n, i))
            print(palindromic)
            if(palindromic != palindromic[::-1]):
                return False
            else:
                continue
        return True
    
solution = Solution()
n = 9
result = solution.isStrictlyPalindromic(n)
print(result)