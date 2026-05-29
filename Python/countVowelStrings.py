class Solution:
    def countVowelStrings(self, n: int) -> int:
        list = [1, 1, 1, 1, 1]
        for i in range(1, n):

            for j in range(3, -1, -1):
                list[j] += list[j + 1]
        
        return sum(list)

solution = Solution()
n = 2
result = solution.countVowelStrings(n)
print(result)