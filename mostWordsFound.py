class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        length = 0
        for words in sentences:
            counter = 1
            for word in words:          
                if(word == " "):
                    counter += 1
            print(counter)
            if(counter > length):
                length = counter
        return length
solution = Solution()
sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
result = solution.mostWordsFound(sentences)
print(result)