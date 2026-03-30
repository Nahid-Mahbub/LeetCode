class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return str(num)
        array = ""

        negative  = num < 0
        num = abs(num)

        while num > 0:
            array = str(num % 7) + array
            num //= 7
        return "-" + array if negative else array

solution = Solution()
num = 7
result = solution.convertToBase7(num)
print(result)