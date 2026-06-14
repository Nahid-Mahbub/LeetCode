class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        lenFirst = 0
        tempMatrix = tempMatrix = [row[:] for row in matrix]
        for i in range(len(matrix)-1, -1, -1):
            for j in range(len(matrix[i])):
                tempMatrix[j][lenFirst] = matrix[i][j]
            print(tempMatrix)
            lenFirst += 1

        matrix.clear()
        matrix.extend(tempMatrix)

solution = Solution()
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
solution.rotate(matrix)
print(matrix)