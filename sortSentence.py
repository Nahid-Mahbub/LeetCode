class Solution:
    def sortSentence(self, s: str) -> str:
        
        split = list(s.split())
        answer = split.copy()
        for word in split:
            print(word[-1], type(word[-1]))
            answer[(int(word[-1]) - 1)] = word[:len(word)-1]
        print(answer)
        return " ".join(answer)
solution = Solution()
s = "lGaWqAkfVIFhqBzRs3 l2 bwKhelcNiyNBpjGUN1"
result = solution.sortSentence(s)
print(result)