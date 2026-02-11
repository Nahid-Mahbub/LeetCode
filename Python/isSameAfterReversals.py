class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        strNum = str(num)
        reversedNum = int(strNum[::-1])
        print(reversedNum, num)
        return str(num) == str(reversedNum)[::-1]

solution = Solution()
num = 526
result = solution.isSameAfterReversals(num)
print(result)