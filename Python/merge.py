class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        
        intervals.sort(key=lambda x: x[0])
        print(intervals)
        
        i = 1
        while i < len(intervals):
            if (intervals[i-1][1] >= intervals[i][0]):
                intervals[i-1][1] = max(intervals[i-1][1], intervals[i][1])
                intervals.pop(i)
            else:
                i += 1           
                    
        return intervals

solution = Solution()
intervals = [[1,4],[4,5]]
result = solution.merge(intervals)
print(result)