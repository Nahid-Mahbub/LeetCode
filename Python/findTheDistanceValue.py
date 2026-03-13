class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        counter = 0
        for x in arr1:
            flag = False
            for y in arr2:
                if (abs(x - y) <= d):
                    flag = True
                    break
            if (flag == False):
                counter += 1
        return counter
                    

solution = Solution()
arr1 = [4,5,8]
arr2 = [10,9,1,8]
d = 2
result = solution.findTheDistanceValue(arr1, arr2, d)
print(result)