class Solution:
    def interpret(self, command: str) -> str:
        for char in command:
            print(char)

solution = Solution()
command = "G()(al)"
result = solution.interpret(command)
print(result)