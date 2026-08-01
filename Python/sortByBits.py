class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))
        # dict = {}
        # for i in arr:
        #     dict[i] = bin(i).count('1')
        # return sorted(arr, key=lambda x: (dict[x], x))

solution = Solution()
arr = [0,1,2,3,4,5,6,7,8]
result = solution.sortByBits(arr)
print(result)