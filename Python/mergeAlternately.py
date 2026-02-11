class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = []
        i = 0
        j = 0
        lenWord1 = len(word1)
        lenWord2 = len(word2)
        print(lenWord1, lenWord2)
        while True:
            if(i < lenWord1):
                output.append(word1[i])
                i += 1
            if(j < lenWord2):
                output.append(word2[j])
                j += 1
            if(i == lenWord1 and j == lenWord2):
                break
        return "".join(output)

solution = Solution()
word1 = "abc"
word2 = "pqr"
result = solution.mergeAlternately(word1, word2)
print(result)