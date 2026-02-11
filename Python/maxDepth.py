class Solution:
    def maxDepth(self, s: str) -> int:
        maxLen = 0
        stack = []
        for char in s:
            if(char == '('):
                stack.append(char)
                if(len(stack) > maxLen):
                    maxLen = len(stack)
            elif(char == ')'):
                stack.pop()
        return maxLen

solution = Solution()
s = "(1+(2*3)+((8)/4))+1"
result = solution.maxDepth(s)
print(result)