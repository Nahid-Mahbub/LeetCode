class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s_list = list(s)
        # for word in t:
        #     if word in s_list:
        #         s_list.remove(word)
        #     else:
        #         return False
        # if len(s_list) == 0:
        #     return True
        # return False

        # Sorted solution
        return sorted(s) == sorted(t)
solution = Solution()
s = "a"
t = "ab"
result = solution.isAnagram(s, t)
print(result)