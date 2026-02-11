import math
class Solution:
    def mySqrt(self, x: int) -> int:
        return int(math.sqrt(x))
solution = Solution()
x = 4
result = solution.mySqrt(x)
print(result)