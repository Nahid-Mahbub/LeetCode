class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num = int(a, 2) + int(b, 2)
        return str(bin(num)[2:])
solution = Solution()
a = "11"
b = "1"
result = solution.addBinary(a, b)
print(result)