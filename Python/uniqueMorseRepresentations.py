class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        morseCode = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        morseCode_set = set()
        for i in range(len(words)):
            pushList = ""
            for j in range(len(words[i])):
                # pushList.append(morseCode[ord(words[i][j])-97])
                # print(morseCode[ord(words[i][j])-97])
                pushList += "".join(morseCode[ord(words[i][j])-97])
            # print(pushList)
            morseCode_set.add(pushList)

        return len(morseCode_set)
solution = Solution()
words = ["rwjje","aittjje","auyyn","lqtktn","lmjwn"]
result = solution.uniqueMorseRepresentations(words)
print(result)