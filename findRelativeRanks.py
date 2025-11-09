class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        rank = sorted(score, reverse = True)
        answer = []
        print(rank, score)
        for num in score:
            for i in range(len(rank)):
                if(num == rank[i]):
                    if(i == 0):
                        answer.append("Gold Medal")
                    elif(i == 1):
                        answer.append("Silver Medal")
                    elif(i == 2):
                        answer.append("Bronze Medal")
                    else:
                        answer.append(str(i+1))
        return answer
    
solution = Solution()
score = [10,3,8,9,4]
result = solution.findRelativeRanks(score)
print(result)