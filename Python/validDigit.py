class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        str_n = str(n)
        str_x = str(x)
        for i in range(len(str_n)):
            if str_n[i] == str_x and i != 0:
                return True
            elif str_n[i] == str_x and i == 0:
                return False
        return False
solution = Solution()
n = 202
x = 2
result = solution.validDigit(n, x)
print(result)