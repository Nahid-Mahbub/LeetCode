class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        output = []
        num_1 = int(s.count("1"))
        for i in range(len(s)):
            if (num_1 != 1 and i < len(s) - 1):
                output.append(1)
                num_1 -= 1
            elif(num_1 == 1 and i < len(s) - 1):
                output.append(0)
            else:
                output.append(1)
        return "".join(map(str, output))

solution = Solution()
s = "0101"
result = solution.maximumOddBinaryNumber(s)
print(result)