class Solution:
    def trap(self, height: list[int]) -> int:
        length = len(height)
        left = 0
        right = length - 1
        maxleft = 0
        maxright = 0
        leftHigh = []
        rightHigh = []
        trap = 0
        while left < length:
            leftHigh.append(maxleft)
            rightHigh.insert(0, maxright)
            if(maxleft < height[left]):
                maxleft = height[left]
            if(maxright < height[right]):
                maxright = height[right]            
            left += 1
            right -= 1
            
        for i in range(len(height)):
            if(0 < min(leftHigh[i], rightHigh[i]) - height[i]):
                trap += min(leftHigh[i], rightHigh[i]) - height[i]
        return trap
solution = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
result = solution.trap(height)
print(result)