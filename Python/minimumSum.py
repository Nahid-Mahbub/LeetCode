class Solution:
    def minimumSum(self, num: int) -> int:
        numList = []
        strNums = str(num)
        for digit in strNums:
            numList.append(int(digit))
        numList.sort()

        # Oneline Sorted [ digits = sorted([int(d) for d in str(num)]) ]
        new1 = numList[0] * 10 + numList[2]
        new2 = numList[1] * 10 + numList[3]

        return new1 + new2
solution = Solution()
num = 2932
result = solution.minimumSum(num)
print(result)