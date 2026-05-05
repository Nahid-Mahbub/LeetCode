class Solution:
    def maxDistToClosest(self, seats: list[int]) -> int:
        left = 0
        mid = 0
        right = 0
        temp = 0
        first_one_found = False

        for seat in seats:
            if(seat == 0):
                temp += 1
            
            else:
                if not first_one_found:
                    left = temp
                    first_one_found = True
                else:
                    mid = max(mid, (temp + 1) // 2)

                temp = 0
        right = temp

        return max(right, left, mid)

solution = Solution()
seats = [1,0,0,0,1,0,1]
result = solution.maxDistToClosest(seats)
print(result)