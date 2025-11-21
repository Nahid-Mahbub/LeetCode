class Solution:
    def reverseDegree(self, s: str) -> int:
        product = 0
        for i in range(1, len(s) + 1):
            # product += ()
            product += (123 - ord(s[i - 1])) * i
        return product
solution = Solution()
s = "abc"
result = solution.reverseDegree(s)
print(result)