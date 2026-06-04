class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        result = []
        for i in range(1, n+1):
            result.append(str(i))
        result.sort()
        int_result = []
        for i in result:
            int_result.append(int(i))
        return int_result

solution = Solution()
n = 13
result = solution.lexicalOrder(n)
print(result)