class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        answer = []
        sortedArr = sorted(list(set(arr)))
        ranks = {}
        for i in range(len(sortedArr)):
            ranks[sortedArr[i]] = i+1
        for num in arr:
            answer.append(ranks[num])
            
        # for num in arr:
        #     for i in range(len(sortedArr)):
        #         if(sortedArr[i] == num):
        #             answer.append(i+1)            
        return answer
solution = Solution()
arr = [40,10,20,30]
result = solution.arrayRankTransform(arr)
print(result)