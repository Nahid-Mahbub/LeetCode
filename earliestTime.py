class Solution:
    def earliestTime(self, tasks: list[list[int]]) -> int:
        output = 201
        for time in tasks:
            if(sum(time) < output):
                output = sum(time)
        return output
solution = Solution()
tasks = [[1,6],[2,3]]
result = solution.earliestTime(tasks)
print(result)