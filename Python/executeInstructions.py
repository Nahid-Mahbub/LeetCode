class Solution:
    def executeInstructions(self, n: int, startPos: list[int], s: str) -> list[int]:
        counter = 0
        for char in s:
            print(char)
            if (char == 'R' and startPos[1] < n-1):
                startPos[1] = startPos[1] + 1
                counter += 1
            elif (char == 'L' and startPos[1] > 0):
                startPos[1] = startPos[1] - 1
                counter += 1
            elif (char == 'U' and startPos[0] > 0):
                startPos[0] = startPos[0] - 1
                counter += 1
            elif (char == 'D' and startPos[0] < n-1):
                startPos[0] = startPos[0] + 1
                counter += 1
            else:
                return counter
        return counter

solution = Solution()
n = 3
startPos = [0,1]
s = "RRDDLU"
result = solution.executeInstructions(n, startPos, s)
print(result)