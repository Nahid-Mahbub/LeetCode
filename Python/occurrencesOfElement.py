class Solution:
    def occurrencesOfElement(self, nums: list[int], queries: list[int], x: int) -> List[int]:
        
        counter = []
        result = []
        for i in range(len(nums)):
            if nums[i] == x:
                counter.append(i)
        print(counter)
        for query in queries:
            if query-1 < len(counter):
                result.append(counter[query-1])
            else:
                result.append(-1)
        return result


solution = Solution()
nums = [1,3,1,7]
queries = [1,3,2,4]
x = 1
result = solution.occurrencesOfElement(nums, queries, x)
print(result)