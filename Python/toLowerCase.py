class Solution:
    def toLowerCase(self, s: str) -> str:
        answer = []
        for char in s:
            if(ord(char) < 91 and ord(char) > 64):
                answer.append(chr(ord(char) + 32))
            else:
                answer.append(char)
        print(ord("Z"))
        return "".join(answer)
solution = Solution()
s = "al&phaBET"
result = solution.toLowerCase(s)
print(result)