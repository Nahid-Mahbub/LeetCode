class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        result = []
        chars = ['a', 'b', 'c']
        def backtrack(current):
            if(len(current) == n):
                result.append(current)
                return
            for ch in chars:
                if not current or current[-1] != ch:
                    backtrack(current + ch)
        backtrack("")
        if(len(result) < k):
            return ""
        return result[k - 1]
solution = Solution()
n = 1
k = 3
result = solution.getHappyString(n, k)
print(result)