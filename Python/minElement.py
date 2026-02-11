class Solution:
    def minElement(self, nums: list[int]) -> int:
        answer = float('inf')
        sum_digits = 0
        for num in nums:
            temp = str(num)
            for digits in temp:
                sum_digits += int(digits)
            if sum_digits < answer:
                answer = sum_digits
            sum_digits = 0
        return answer
            
solution = Solution()
nums = [999,19,199]
result = solution.minElement(nums)
print(result)