class Solution:
    def maximumNumberOfStringPairs(self, words: list[str]) -> int:
        counter = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if(words[i] == words[j][::-1]):
                    counter += 1
        return counter
solution = Solution()
words = ["cd","ac","dc","ca","zz"]
result = solution.maximumNumberOfStringPairs(words)
print(result)