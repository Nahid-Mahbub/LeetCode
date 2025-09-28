class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        length = len(prices)
        for i in range(length):
            for j in range(i+1, length):
                if(prices[i] >= prices[j]):
                    print(prices[i], prices[j], i, j)
                    prices[i] -= prices[j]
                    break
        return prices
solution = Solution()
prices = [8,4,6,2,3]
result = solution.finalPrices(prices)
print(result)