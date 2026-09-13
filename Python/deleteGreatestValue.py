class Solution:
    def deleteGreatestValue(self, grid: list[list[int]]) -> int:
        total_sum = 0
        for row in grid:
            row.sort(reverse=True)
        for col in range(len(grid[0])):
            max_value = max(grid[row][col] for row in range(len(grid)))
            total_sum += max_value
        return total_sum
    
solution = Solution()
grid = [[1,2,4],[3,3,1]]
result = solution.deleteGreatestValue(grid)
print(result)