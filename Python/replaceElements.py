class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        # for i in range(len(arr)-1):
        #     maxInt = 0
        #     for j in range(i+1, len(arr)):
        #         if( maxInt < arr[j]):
        #             maxInt = arr[j]
        #     arr[i] = maxInt
        # arr[len(arr)-1] = -1
        # return arr
        maxRight = -1
        for i in range(len(arr)-1, -1, -1):
            current = arr[i]
            arr[i] = maxRight
            maxRight = max(current, maxRight)
        return arr
    
soultion = Solution()
arr = [17,18,5,4,6,1]
result = soultion.replaceElements(arr)
print(result)