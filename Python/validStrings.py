class Solution:
    def validStrings(self, n: int) -> list[str]:
        result = []
        subSet = []
        
        def dfs(i):
            if (i == n):
                result.append("".join(subSet))
                return
            
            subSet.append('1')
            dfs(i + 1)
            subSet.pop()

            if (not subSet or subSet[-1] == '1'):
                subSet.append('0')
                dfs(i + 1)
                subSet.pop()
        dfs(0)
        return result
    
solution = Solution()
n = 4
result = solution.validStrings(n)
print(result)