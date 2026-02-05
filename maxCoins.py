class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        piles.sort()
        print(piles)
        output = 0
        i = len(piles) - 2
        for _ in range(len(piles)//3):
            output += piles[i]
            i -= 2
        return output
    
solution = Solution()
piles = [9,8,7,6,5,1,2,3,4]
result = solution.maxCoins(piles)
print(result)