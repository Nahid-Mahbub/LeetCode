class Solution:
    def executeInstructions(self, n: int, startPos: list[int], s: str) -> list[int]:
        
        result = []
        for i in range(len(s)):
            x, y = startPos
            counter = 0

            for j in range(i, len(s)):
                if s[j] == 'R':
                    y += 1
                elif s[j] == 'L':
                    y -= 1
                elif s[j] == 'U':
                    x -= 1
                elif s[j] == 'D':
                    x += 1
                
                if x < 0 or x >= n or y < 0 or y >= n:
                    break
                
                counter += 1
            
            result.append(counter)
            
        return result

solution = Solution()
n = 3
startPos = [0,1]
s = "RRDDLU"
result = solution.executeInstructions(n, startPos, s)
print(result)