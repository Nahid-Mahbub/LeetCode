class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        counter = 0
        ans = x ^ y
        ans = bin(ans)
        ans = ans[2:]
        for i in range(len(ans)):
            if(ans[i] == "1"):
                counter += 1
        return counter
solution = Solution()
x = 1
y = 4
result = solution.hammingDistance(x, y)
print(result)