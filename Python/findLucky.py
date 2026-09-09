class Solution:
    def findLucky(self, arr: list[int]) -> int:
        dic_count = {}
        result = [-1]
        for num in arr:
            dic_count[num] = dic_count.get(num, 0) + 1
        print(dic_count)
        for key, value in dic_count.items():
            if key == value:
                result.append(key)
        result.sort(reverse=True)
        return result[0]

solution = Solution()
arr = [4,3,2,2,4,1,3,4,3]
result = solution.findLucky(arr)
print(result)