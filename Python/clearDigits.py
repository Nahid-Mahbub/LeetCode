class Solution:
    def clearDigits(self, s: str) -> str:
        digits = "0123456789"
        result = []
        for char in s:
            if char not in digits:
                result.append(char)
            else:
                result.pop()
        return ''.join(result)                
        

solution = Solution()
s = "abc"
result = solution.clearDigits(s)
print(result)