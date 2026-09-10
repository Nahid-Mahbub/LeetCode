class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        blank_count = moves.count('_')
        l_count = moves.count('L')
        r_count = moves.count('R')
        return abs(l_count - r_count) + blank_count
            
solution = Solution()
moves = "L_RL__R"
result = solution.furthestDistanceFromOrigin(moves)
print(result)