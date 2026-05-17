class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)

            sum = 0
            for num in str(n):
                sum += int(num) ** 2
            print(sum)
            n = sum
        return n == 1
            

solution = Solution()
n = 2
result = solution.isHappy(n)
print(result)