class Solution:
    def rotateTheBox(self, boxGrid: list[list[str]]) -> list[list[str]]:
        
        print(boxGrid)
        print()
        for i in range(len(boxGrid)):
            j = len(boxGrid[i]) - 1
            for j in range(len(boxGrid[i])-1, -1, -1):
                if (boxGrid[i][j] == '.'):
                    if (boxGrid[i][j-1] == "*" or j == 0):
                        continue
                    
                    temp = boxGrid[i][j]
                    boxGrid[i][j] = boxGrid[i][j-1]
                    boxGrid[i][j-1] = temp
                    print(boxGrid)
        print(boxGrid)
        print()
        result = []
        for i in range(len(boxGrid[0])):
            temp = []
            for j in range(len(boxGrid)-1, -1, -1):
                temp.append(boxGrid[j][i])

            result.append(temp)
        return result
    
solution = Solution()
boxGrid = [["#","#","*",".","*","."],["#","#","#","*",".","."],["#","#","#",".","#","."]]
result = solution.rotateTheBox(boxGrid)
print(result)