class Solution:
    def sortTheStudents(self, score: list[list[int]], k: int) -> list[list[int]]:
        output = []
        tempIndex = {}
        for i in range(len(score)):
            tempIndex[i] = score[i][k]
        keyList = sorted(tempIndex, key = tempIndex.get, reverse = True)
        for num in keyList:
            tempList = []
            for i in range(len(score[num])):
                tempList.append(score[num][i])
            output.append(tempList)
        return output
    
solution = Solution()
score = [[10,6,9,1],[7,5,11,2],[4,8,3,15]]
k = 2
result = solution.sortTheStudents(score, k)
print(result)