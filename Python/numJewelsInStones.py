class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = 0
        jewels_set = set()
        for jewel in jewels:
            jewels_set.add(jewel)
        for stone in stones:
            if(stone in jewels_set):
                counter += 1
        return counter
solution = Solution()
jewels = "aA"
stones = "aAAbbbb"
result = solution.numJewelsInStones(jewels, stones)
print(result)