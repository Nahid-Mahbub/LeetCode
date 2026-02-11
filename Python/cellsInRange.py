class Solution:
    def cellsInRange(self, s: str) -> list[str]:
        staring = ord(s[0])
        ending = ord(s[3])
        output = []
        for i in range(staring, ending+1):
            for j in range(int(s[1]), int(s[4])+1):
                output.append(chr(i)+str(j))
        return output
solution = Solution()
s = "K1:L2"
result = solution.cellsInRange(s)
print(result)