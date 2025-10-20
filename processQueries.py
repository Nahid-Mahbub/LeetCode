class Solution:
    def processQueries(self, queries: list[int], m: int) -> list[int]:
        mRange = [i for i in range(1, m+1)]
        counter = []
        for querie in queries:
            for i in range(len(mRange)):
                if(querie == mRange[i]):
                    print(i)
                    counter.append(i)                   
                    mRange.insert(0, mRange.pop(mRange[i]))
                    print(mRange)
        return counter

solution = Solution()
queries = [3,1,2,1]
m = 5
result = solution.processQueries(queries, m)
print(result)