class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        str_n = str(n)
        additon = 0
        production = 1
        for num in str_n:
            production *= int(num)
            additon += int(num)
        return production - additon
solution = Solution()
n = 4421
result = solution.subtractProductAndSum(n)
print(result)