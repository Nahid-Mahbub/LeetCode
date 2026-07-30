class Solution:
    def isPrime(self, num: int) -> bool:
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    def sumOfPrimesInRange(self, n: int) -> int:
        total = 0
        reversedInt = int(str(n)[::-1])
        if reversedInt > n:
            temp = n
            n = reversedInt
            reversedInt = temp
        for i in range(reversedInt, n + 1):
            if self.isPrime(i):
                total += i
        return total

solution = Solution()
n = 13
result = solution.sumOfPrimesInRange(n)
print(result)