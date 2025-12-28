class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        sortedS = sorted(s)
        setS = set(sortedS)
        length = len(sortedS) / len(setS)
        for char in setS:
            if(sortedS.count(char) != length):
                return False
        return True
solution = Solution()
s = "abacbc"
result = solution.areOccurrencesEqual(s)
print(result)