class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        xor = start
        for i in range(1, n):
            val = start + 2 * i
            xor ^= val
        return xor
solution = Solution()
n = 4
start = 3
result = solution.xorOperation(n, start)
print(result)