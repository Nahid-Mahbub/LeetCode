class Solution:
    def sortMatrix(self, grid: list[list[int]]) -> list[list[int]]:
        
        row = len(grid)
        column = len(grid[0])
        flag = False
        result = [[0 for _ in range(column)] for _ in range(row)]

        for diagonals in range(row + column - 1):
            diagonal = []
            for r in range(row):
                c = diagonals - (row -1 -r)

                if (0 <= c < column):
                    diagonal.append(grid[r][c])
            print(diagonal)
            if (len(diagonal) == row or flag):
                
                if not flag:
                    diagonal.sort(reverse=True)
                else:
                    diagonal.sort()
                flag = True
            else:
                diagonal.sort(reverse=True)
            print(diagonal)
            i = 0
            for r in range(row):
                c = diagonals - (row - 1 -r)
                if (0 <= c < column):
                    result[r][c] = diagonal[i]
                    i += 1
            print(result)
        return result


solution = Solution()
grid = [[1,7,3],[9,8,2],[4,5,6]]
result = solution.sortMatrix(grid)
print(result)