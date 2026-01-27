class Solution:
    def countGoodTriplets(self, arr: list[int], a: int, b: int, c: int) -> int:
        output = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if (abs(arr[i] - arr[j]) <= a):
                    for k in range(j+1, len(arr)):
                        if(abs(arr[j] - arr[k]) <= b):
                            if(abs(arr[i] - arr[k]) <= c):
                                output += 1
        return output
    
solution = Solution()
arr = [3,0,1,1,9,7]
a = 7
b = 2
c = 3
result = solution.countGoodTriplets(arr, a, b, c)
print(result)