class Solution:
    def frequencySort(self, s: str) -> str:
        
        result = ""
        freq = {}
        for char in s:
            if (char in freq):
                freq[char] += 1
            else:
                freq[char] = 1
                
        print(freq)
        sorted_freq = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))
        print(sorted_freq)

        for char, count in sorted_freq.items():
            result += char*count
        return result


solution = Solution()
s = "tree"
result = solution.frequencySort(s)
print(result)