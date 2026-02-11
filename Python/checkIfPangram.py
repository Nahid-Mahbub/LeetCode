class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alchabet = set(sentence)
        if(len(alchabet) != 26):
            return False    
        else:
            return True
solution = Solution()
sentence = "thequickbrownfoxjumpsoverthelazydog"
result = solution.checkIfPangram(sentence)
print(result)