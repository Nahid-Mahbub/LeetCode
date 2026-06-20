class Solution:
    def rotateTheBox(self, boxGrid: list[list[str]]) -> list[list[str]]:
        
        print(boxGrid)
        print()
        boxGrid_len = len(boxGrid)
        boxGrid0_len = len(boxGrid[0])
        for i in range(boxGrid_len):
            gravity = boxGrid0_len - 1
            for j in range(boxGrid0_len-1, -1, -1):
                if (boxGrid[i][j] == '*'):
                    gravity = j - 1
                elif (boxGrid[i][j] == '#'):
                    boxGrid[i][j] = '.'
                    boxGrid[i][gravity] = '#'
                    gravity -= 1
                    print(boxGrid)
        
        print()
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