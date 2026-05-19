class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        dict_vowels = {'a', 'e', 'i', 'o', 'u'}
        for i in range(len(s) - 1, -1, -1):
            if s[i] not in dict_vowels:
                return s[:i + 1]
        return ""

solution = Solution()
s = "idea"
result = solution.trimTrailingVowels(s)
print(result)