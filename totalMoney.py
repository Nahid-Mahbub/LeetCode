class Solution:
    def totalMoney(self, n: int) -> int:
        bank = 0
        initial = 1
        i = 1
        j = 1
        # while i <= n:
        #     if((i%7) == 0):
        #         bank += j
        #         initial += 1
        #         j = initial
        #         i += 1
        #         continue
        #     bank += j
        #     i += 1
        #     j += 1

        for i in range(1, n+1):
            if((i%7) == 0):
                bank += j
                initial += 1
                j = initial
                continue
            bank += j
            j += 1
        return bank

solution = Solution()
n = 10
result = solution.totalMoney(n)
print(result)