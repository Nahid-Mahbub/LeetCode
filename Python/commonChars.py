class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        wordsList = []
        answer = []
        for word in words:
            wordsList.append(list(word))
        print(wordsList)

        if (len(wordsList) == 1):
            return wordsList[0]
        
        for char in wordsList[0]:
            flag = False
            for i in range(1, len(wordsList)):
                
                if (char in wordsList[i]):
                    wordsList[i].remove(char)
                else:
                    flag = True
            if (flag == False):
                answer.append(char)
        return answer

solution = Solution()
words = ["bella","label","roller"]
result = solution.commonChars(words)
print(result)