from collections import defaultdict
class Solution:
    def diagonalSort(self, mat: list[list[int]]) -> list[list[int]]:
        diagonals = defaultdict(list)
        row = len(mat)
        column = len(mat[0])

        for i in range(row):
            for j in range(column):
                diagonals[i - j].append(mat[i][j])
        
        for d in diagonals:
            diagonals[d].sort(reverse=True)

        for i in range(row):
            for j in range(column):
                mat[i][j] = diagonals[i - j].pop()
        return mat
    
solution = Solution()
mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
result = solution.diagonalSort(mat)
print(result)