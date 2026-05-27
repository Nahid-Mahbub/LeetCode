class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        _digit = str(digit)
        counter = 0
        for num in nums:
            for char in str(num):
                if char == _digit:
                    counter += 1
        return counter

solution = Solution()
nums = [3]
digit = 1
result = solution.countDigitOccurrences(nums, digit)
print(result)