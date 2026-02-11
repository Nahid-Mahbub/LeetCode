class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        answer = []
        for num in candidates:
            if(target % num == 0):
                answer.extend()
        return answer
    
solution = Solution()
candidates = [2,3,6,7]
target = 7
result = solution.combinationSum(candidates, target)
print(result)