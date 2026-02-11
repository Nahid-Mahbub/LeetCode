class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if (ch not in word):
            return word
        index = word.index(ch)
        return word[:index][::-1] + word[index+1::]
solution = Solution()
word = "abcdefd"
ch = "d"
result = solution.reversePrefix(word, ch)
print(result)