class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        
        join1 = "".join(word1)
        join2 = "".join(word2)
        if (join1 == join2):
            return True
        else:
            return False
solution = Solution()
word1 = ["ab", "c"]
word2 = ["a", "bc"]
result = solution.arrayStringsAreEqual(word1, word2)
print(result)