class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        output = []
        for i in range(len(strs)):
            if strs[i] != "-1":
                ans = [strs[i]]
                target = sorted(strs[i])
                strs[i] = "-1"
                for j in range(len(strs)):
                    if(strs[j] != "-1" and target == sorted(strs[j])):
                        ans.append(strs[j])
                        strs[j] = "-1"
                output.append(ans)
        return output

solution = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
result = solution.groupAnagrams(strs)
print(result)