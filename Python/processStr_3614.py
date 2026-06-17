class Solution:
    def processStr(self, s: str, k: int) -> str:
        
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
        if result:
            return result[k]
        else:
            return "."
solution = Solution()
s = "#"
k = 6523

result = solution.processStr(s, k)
print(result)