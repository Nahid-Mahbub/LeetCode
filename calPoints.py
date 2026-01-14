class Solution:
    def calPoints(self, operations: list[str]) -> int:
        output = []
        for detail in operations:
            if(detail == 'C'):
                output.pop()
            elif(detail == 'D'):
                output.append(output[-1] * 2)
            elif(detail == '+'):
                output.append(output[-1] + output[-2])
            else:
                output.append(int(detail))
        return sum(output)
    
solution = Solution()
ops = ["5","2","C","D","+"]
result = solution.calPoints(ops)
print(result)