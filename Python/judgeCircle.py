class Solution:
    def judgeCircle(self, moves: str) -> bool:
        vertical = 0
        horizontal = 0
        for move in moves:
            if(move == "U"):
                vertical += 1
            elif(move == "D"):
                vertical -= 1
            elif(move == "R"):
                horizontal += 1
            else:
                horizontal -= 1
        if(vertical == 0 and horizontal == 0):
            return True
        return False
    
solution = Solution()
moves = "UD"
result = solution.judgeCircle(moves)
print(result)