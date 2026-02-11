class Solution:
    def maxIncreaseKeepingSkyline(self, grid: list[list[int]]) -> int:
        counter = 0
        grid2 = []
        for i in range(len(grid)):
            temp= []
            for j in range(len(grid)):
                temp.append(grid[j][i])
            grid2.append(temp)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                counter += (min(max(grid[i]), max(grid2[j]))) - grid[i][j]
        return counter
solution = Solution()
grid = [[59,88,44],[3,18,38],[21,26,51]]
result = solution.maxIncreaseKeepingSkyline(grid)
print(result)

# AlterNative solution

# class Solution:
#     def maxIncreaseKeepingSkyline(self, grid: list[list[int]]) -> int:
#         row_max = [max(row) for row in grid]
#         col_max = [max(col) for col in zip(*grid)]

#         total = 0
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 total += min(row_max[i], col_max[j]) - grid[i][j]

#         return total
