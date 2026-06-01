class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        
        players = set()
        for winner, loser in matches:
            players.add(winner)
            players.add(loser)

        print(players)
        freq = {player: 0 for player in players}
        for match in matches:
            freq[match[1]] += 1
        
        print(freq)
        winners = []
        losers = []
        for player in freq:
            if freq[player] == 0:
                winners.append(player)
            elif freq[player] == 1:
                losers.append(player)
        return [sorted(winners), sorted(losers)]

solution = Solution()
matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
result = solution.findWinners(matches)
print(result)

