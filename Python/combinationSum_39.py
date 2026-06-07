class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        def backtrack(start, path, total):
            print(f"Path: {path}, Total: {total}")
            if total == target:
                result.append(path.copy())
                return
            if total > target:
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])                

                backtrack(i, path, total + candidates[i])
                
                path.pop()

        backtrack(0, [], 0)
        return result
    
solution = Solution()
candidates = [2,3,6,7]
target = 7
result = solution.combinationSum(candidates, target)
print(result)