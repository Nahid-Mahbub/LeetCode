class Solution:
    def doesValidArrayExist(self, derived: list[int]) -> bool:
        x = 0
        for num in derived:
            x ^= num
        return x == 0
        
solution = Solution()
derived = [1, 1, 0]
result = solution.doesValidArrayExist(derived)
print(result)