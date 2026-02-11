class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        dictionary = {}
        new_list = []
        for i in range(len(heights)):
            dictionary[heights[i]] = names[i]
        heights.sort(reverse = True)
        for height in heights:
            new_list.append(dictionary[height])
        return new_list
solution = Solution()
names = ["Mary","John","Emma"]
heights = [180,165,170]
result = solution.sortPeople(names, heights)
print(result)