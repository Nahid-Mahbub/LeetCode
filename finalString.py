class Solution:
    def finalString(self, s: str) -> str:
        output = []
        for i in range(len(s)):
            if(s[i] == 'i'):
                output = output[::-1]
            else:
                output.append(s[i])
        return "".join(output)
solution = Solution()
s = "string"
result = solution.finalString(s)
print(result)