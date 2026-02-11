class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        index = 1
        odd_sum = 0 
        even_sum = 0
        for i in range(n):
            odd_sum += index
            even_sum += index + 1
            index += 2
        while odd_sum != 0:
            even_sum, odd_sum = odd_sum, even_sum % odd_sum
        return even_sum # return n is also a solution


solution = Solution()
n = 5
result = solution.gcdOfOddEvenSums(n)
print(result)