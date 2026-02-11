class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        myDict = {}
        Ascii = 97
        answer = []
        for char in key:
            if(char != " " and char not in myDict):
                myDict[char] = chr(Ascii)
                # print(chr(Ascii))
                Ascii += 1

        for msg in message:
            if(msg != " "):
                answer.append(myDict[msg])
            else:
                answer.append(" ")
        return "".join(answer)
solution = Solution()
key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"
result = solution.decodeMessage(key, message)
print(result)   