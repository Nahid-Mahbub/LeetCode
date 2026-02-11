class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:        
        answer = []
        def backtrack(start, temp):
            if(len(temp) == k):
                answer.append(temp.copy()) # Here we use copy value because append() will just linked the value then if i change in temp, answer will also changed.
                return
            
            for i in range(start, n + 1):
                temp.append(i)
                backtrack(i+1, temp)
                temp.pop()
        backtrack(1, [])
        return answer
    
solution = Solution()
n = 5
k = 3
result = solution.combine(n, k)
print(result)