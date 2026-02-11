class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        counter = 0
        for word in words:
            compare = set(word)
            flag = 0
            for check in compare:
                if(check not in allowed):
                    flag = 0
                    break
                else:
                    flag = 1
            if(flag == 1):
                counter += 1
        return counter
solution = Solution()
allowed = "abc"
words = ["a","b","c","ab","ac","bc","abc"]
result = solution.countConsistentStrings(allowed, words)
print(result)