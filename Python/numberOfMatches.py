class Solution:
    def numberOfMatches(self, n: int) -> int:
        teams = n
        output = 0
        while teams > 1:            
            matches = (teams//2)
            teams -= matches
            output += matches
            print(matches, teams)
        return output

solution = Solution()
n = 7
result = solution.numberOfMatches(n)
print(result)