class Solution:
    def reverseWords(self, s: str) -> str:
        sSplit = s.split()
        ans = ""
        for i in range(len(sSplit)-1):
            ans += sSplit[i][::-1]
            ans += " "
        ans += sSplit[len(sSplit)-1][::-1]
        return ans
        
solution = Solution()
s = "Let's take LeetCode contest"
result = solution.reverseWords(s)
print(result)