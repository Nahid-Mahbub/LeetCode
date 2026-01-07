class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        vowel_freq = {}
        consonant_freq = {}
        
        for ch in s:
            if ch in vowels:
                vowel_freq[ch] = vowel_freq.get(ch, 0) + 1
            else:
                consonant_freq[ch] = consonant_freq.get(ch, 0) + 1
        
        max_vowel = max(vowel_freq.values()) if vowel_freq else 0
        max_consonant = max(consonant_freq.values()) if consonant_freq else 0
        
        return max_vowel + max_consonant



# Test
solution = Solution()
s = "successes"
result = solution.maxFrequencySum(s)
print(result)  # Output: 6
