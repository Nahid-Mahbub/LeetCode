class Solution:
    def processStr(self, s: str) -> str:
        
        result = []
        for char in s:
            if char.isalnum():
                result.append(char)
            elif char == '#':
                result = result + result
            elif char == "%":
                result.reverse()
            elif char == "*":
                if result:
                    result.pop()

        return ''.join(result)
solution = Solution()
s = "a#b%*"
result = solution.processStr(s)
print(result)