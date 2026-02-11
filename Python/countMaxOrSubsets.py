class Solution:
    def countMaxOrSubsets(self, nums: list[int]) -> int:
        result = []
        subset = []
        counter = []

        def dfs(i):
            # nonlocal counter
            if i >= len(nums):
                result.append(subset.copy())
                subsetCounter = 0
                for num in subset:
                    subsetCounter = subsetCounter | num
                counter.append(subsetCounter)
                return
            
            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        freq = []
        for num in set(counter):
          freq.append(counter.count(num))
        freq.sort()
        return freq[::-1][0]

solution = Solution()
nums = [2, 2, 2]
result = solution.countMaxOrSubsets(nums)
print(result)