class Solution:
    def replaceDigits(self, s: str) -> str:
        listString = list(s)
        for i in range(len(listString)):
            if listString[i].isdigit():
                listString[i] = chr(ord(listString[i-1]) + int(listString[i]))
        return "".join(listString)
    
solution = Solution()
s = "a1c1e1"
result = solution.replaceDigits(s)
print(result)