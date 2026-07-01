class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        
        result = []
        for i in range(len(matrix)):
            
            result.append(sum(matrix[i]))
        return result
solution = Solution()
matrix = [[0,1,0],[1,0,0],[0,0,0]]
result = solution.findDegrees(matrix)
print(result)