class Solution:
    def countPoints(self, rings: str) -> int:

        dic_rods = {}
        answer = []
        for i in range(0, len(rings), 2):
            color = rings[i]
            rod = rings[i + 1]

            if rod not in dic_rods:
                dic_rods[rod] = set()
            dic_rods[rod].add(color)

        
        for i in dic_rods:
            if len(dic_rods[i]) == 3:
                answer.append(i)
        return len(answer)

solution = Solution()
rings = "B0B6G0R6R0R6G9"
result = solution.countPoints(rings)
print(result)