class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        vowel_list = []
        for char in s:
            if char in vowels:
                vowel_list.append(char)
        vowel_list.sort(key = lambda x: ord(x))
        
        result = []
        vowel_index = 0
        for char in s:
            if char in vowels:
                result.append(vowel_list[vowel_index])
                vowel_index += 1
            else:
                result.append(char)
        
        return ''.join(result)

solution = Solution()
s = "lEetcOde"
result = solution.sortVowels(s)
print(result)