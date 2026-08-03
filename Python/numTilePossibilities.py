from collections import Counter
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        def dfs(counter):

            ans = 0
            for ch in counter:
                if counter[ch] == 0:
                    continue
                ans += 1
                counter[ch] -= 1
                ans += dfs(counter)
                counter[ch] += 1
            return ans
        return dfs(Counter(tiles))

solution = Solution()
tiles = "AAB"
result = solution.numTilePossibilities(tiles)
print(result)