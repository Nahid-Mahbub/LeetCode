class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        counter = 0
        # for i in range(len(mat)):
        #     for j in range(len(mat[i])):
        #         if(i == j):
        #             counter += mat[i][j]
        #             print(counter)
        #             if(j != (len(mat[i])-(i+1))):
        #                 counter += mat[i][len(mat[i])-(i+1)]
        #                 print(counter)
        #             print(mat[i][j])
        #             print(mat[i][len(mat[i])-(i+1)])
        #             print("Value of counter: ",counter)
        for i in range(len(mat)):
            counter += mat[i][i]
            if(i != (len(mat[i])-(i+1))):
                counter += mat[i][len(mat[i]) - (i+1)]
        return counter
solution = Solution()
mat = [[1,2,3], [4,5,6], [7,8,9]]
result = solution.diagonalSum(mat)
print(result)