class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        
        for word in words:
            if(word[::-1] == word):
                return word
        return ""
solution = Solution()
words = ["abc","car","ada","racecar","cool"]
result = solution.firstPalindrome(words)
print(result)