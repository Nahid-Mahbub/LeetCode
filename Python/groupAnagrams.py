from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        output = defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))
            output[key].append(word)
        return list(output.values())
    
solution = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
result = solution.groupAnagrams(strs)
print(result)