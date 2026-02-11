class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        n = len(boxes)
        ans = [0]*n

        balls = 0
        shift = 0
        for right in range(n):
            ans[right] = shift
            if (boxes[right] == "1"):
                balls += 1
            shift += balls
            
        balls = 0
        shift = 0
        for left in range(n-1, -1, -1):
            ans[left] += shift
            if(boxes[left] == "1"):
                balls += 1
            shift += balls
        return ans



        


solution = Solution()
boxes = "001011"
result = solution.minOperations(boxes)
print(result)