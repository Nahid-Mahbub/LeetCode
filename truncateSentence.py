class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        words = s.split()
        array = ""
        if(k < len(words)):
            words.pop(k)
            array = " ".join(words[:k])
        else:
            array = " ".join(words)
        return array
solution = Solution()
s = "Hello how are you Contestant"
k = 4
result = solution.truncateSentence(s, k)
print(result)