class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        valid = []
        for list in matrix:
            minimum = min(list)
            index = list.index(minimum)
            for i in range(len(matrix)):
                if(matrix[i][index] > minimum):
                    break
                elif(i == len(matrix)-1):
                    valid.append(minimum)
        return valid

solution = Solution()
matrix = [[3,7,8],[9,11,13],[15,16,17]]
result = solution.luckyNumbers(matrix)
print(result)