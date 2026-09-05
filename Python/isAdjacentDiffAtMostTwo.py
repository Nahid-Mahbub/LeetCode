class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:

        for i in range(len(s) - 1):
            if abs(ord(s[i]) - ord(s[i + 1])) > 2:
                return False
        return True
    
solution = Solution()
input_string = "abcde"
result = solution.isAdjacentDiffAtMostTwo(input_string)
print(f"Is the adjacent difference at most two for '{input_string}'? {result}")