class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        sort_heights = sorted(heights)
        counter = 0
        for i in range(len(heights)):
            if(heights[i] != sort_heights[i]):
                counter += 1
        return counter
solution = Solution()
heights = [1,1,4,2,1,3]
result = solution.heightChecker(heights)
print(result)