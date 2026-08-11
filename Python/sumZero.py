class Solution:
    def sumZero(self, n: int) -> list[int]:
        arr = []
        if n < 2:
            arr.append(0)
        else:
            if n % 2 != 0:
                for i in range(-(n // 2), n // 2 + 1):
                    arr.append(i)
                    
            else:
                for i in range(1, (n // 2) + 1):
                    arr.append(i)
                    arr.append(-i)
        return arr
    
solution = Solution()
n = 0
result = solution.sumZero(n)
print(result)