class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        answer = 0
        lenPref = len(pref)
        for word in words:
            if(pref == word[:lenPref]):
                answer += 1
        return answer
solution = Solution()
words = ["pay","attention","practice","attend"]
pref = "at"
result = solution.prefixCount(words, pref)
print(result)