class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        ans = [pref[0]]
        for i in range(1, len(pref)):
            ans.append(pref[i-1] ^ pref[i])
            print(pref[i-1], pref[i])
        return ans

solution = Solution()
pref = [13]
result = solution.findArray(pref)
print(result)