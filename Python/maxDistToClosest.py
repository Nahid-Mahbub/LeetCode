class Solution:
    def maxDistToClosest(self, seats: list[int]) -> int:
        int current = 0
        for seat in seats:
            
solution = Solution()
seats = [1,0,0,0,1,0,1]
result = solution.maxDistToClosest(seats)
print(result)