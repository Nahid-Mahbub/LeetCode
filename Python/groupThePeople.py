class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        length = len(groupSizes)
        group_list = []
        init_val = 0
        while(length*-1 != sum(groupSizes)):
            ans = []
            for size in groupSizes:
                if(size != -1):
                    init_val = size
                    break
            for i in range(length):
                if(groupSizes[i] == init_val):
                    ans.append(i)
                    groupSizes[i] = -1
                if(len(ans) == init_val):
                    break
            group_list.append(ans)
        return group_list

solution = Solution()
groupSizes = [3,3,3,3,3,1,3]
result = solution.groupThePeople(groupSizes)
print(result)