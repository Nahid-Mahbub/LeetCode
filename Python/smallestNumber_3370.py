class Solution:
    def smallestNumber(self, n: int) -> int:
        num_bin = bin(n)[2:]  
        if '0' in num_bin:
            return int(num_bin.replace('0', '1'), 2)
        else:
            return int(num_bin, 2)
            
solution = Solution()
input = 3
result = solution.smallestNumber(input)
print(f"The smallest number with {input} digits is: {result}")