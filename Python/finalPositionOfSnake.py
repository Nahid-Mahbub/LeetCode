class Solution:
    def finalPositionOfSnake(self, n: int, commands: list[str]) -> int:
        output = 0
        for i in range(len(commands)):
            if(commands[i] == "RIGHT"):
                output += 1
            elif(commands[i] == "LEFT"):
                output -= 1
            elif(commands[i] == "DOWN"):
                output += n
            else:
                output -= n
        return output

solution = Solution()
n = 3
commands = ["DOWN","RIGHT","UP"]
result = solution.finalPositionOfSnake(n, commands)
print(result)