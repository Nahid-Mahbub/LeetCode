class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        
        for i in range(len(arr)):
            for j in range(len(arr)):
                if(i != j):
                    if(arr[i] == arr[j] * 2):
                        return True
        return False
solution = Solution()
arr = [10,2,5,3]
result = solution.checkIfExist(arr)
print(result)