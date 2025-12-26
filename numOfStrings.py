class Solution:
    def numOfStrings(self, patterns: list[str], word: str) -> int:
        subWord = []
        counter = 0
        for i in range(len(word)):
            for j in range(i + 1, len(word) + 1):
                subWord.append(word[i:j])
        for char in patterns:
            if(char in subWord):
                counter += 1
        return counter
    
solution = Solution()
patterns = ["a","abc","bc","d"]
word = "abc"
result = solution.numOfStrings(patterns, word)
print(result)