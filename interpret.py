class Solution:
    def interpret(self, command: str) -> str:
        output = []
        for i in range(len(command)):
            if(command[i] == '('):
                if(command[i + 1] == 'a'):
                    continue
                elif(command[i + 1] == ')'):
                    output.append('o')
            elif(command[i] == ')'):
                continue
            else:
                output.append(command[i])
        return "".join(output)
    
solution = Solution()
command = "G()(al)"
result = solution.interpret(command)
print(result)