class Solution:
    def maxArea(self, height: list[int]) -> int:
        
        left = 0
        right = len(height) - 1
        tempLeft = 0
        maxArea = 0
        while left < right:
            if(maxArea < (right - left) * min(height[left], height[right])):
                maxArea = (right - left) * min(height[left], height[right])
            if(height[left] < height[right]):
                left += 1
            else:
                right -= 1
        return maxArea
solution = Solution()
height = [1,1]
result = solution.maxArea(height)
print(result)