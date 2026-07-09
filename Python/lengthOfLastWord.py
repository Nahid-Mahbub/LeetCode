class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_word_length = 0
        sList = s.split()
        if sList:
            last_word_length = len(sList[-1])
        return last_word_length
            
solution = Solution()
s = "   fly me   to   the moon  "
result = solution.lengthOfLastWord(s)
print(result)