class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = list(range(1, n + 1))
        index = 0
        
        while len(players) > 1:
            index = (index + k - 1) % len(players)
            players.pop(index)
        
        return players[0]


solution = Solution()
n = 5
k = 2
result = solution.findTheWinner(n, k)
print(result)