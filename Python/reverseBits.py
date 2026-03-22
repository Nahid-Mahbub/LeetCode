class Solution:
    def reverseBits(self, n: int) -> int:
        binary = format(n, "032b")
        return int(binary[::-1], 2)
        
solution = Solution()
n = 43261596
result = solution.reverseBits(n)
print(result)