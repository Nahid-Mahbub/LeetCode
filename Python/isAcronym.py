class Solution:
    def isAcronym(self, words: list[str], s: str) -> bool:
        if (len(s) != len(words)):
            return False
        for i in range(len(s)):
            if(s[i] != words[i][:1]):
                return False
        return True
solution = Solution()
words = ["alice","bob","charlie"]
s = "abc"
result = solution.isAcronym(words, s)
print(result)