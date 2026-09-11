class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if (len(target) != len(arr)):
            return False
        target.sort()
        arr.sort()

        for i in range(len(target)):
            if(target[i] != arr[i]):
                return False
        return True

solution = Solution()
target = [1,2,3,4]
arr = [2,4,1,3]
result = solution.canBeEqual(target, arr)
print(result)
