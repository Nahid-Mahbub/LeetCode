class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        
        result = 0
        freq = {}
        for num in str(n):
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        print(freq)
        for char, count in freq.items():
            result += int(char) * count
        return result
    
solution = Solution()
n = 122
result = solution.digitFrequencyScore(n)
print(result)