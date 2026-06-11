class Solution(object):
    def garbageCollection(self, garbage, travel):
        """
        :type garbage: List[str]
        :type travel: List[int]
        :rtype: int
        """
        totalTime = 0
        flagG = False
        flagP = False
        flagM = False

        for temp in garbage:
            totalTime += len(temp)
        
        for i in range(len(garbage)-1, -1, -1):
            if "G" in garbage[i] and not flagG:
                totalTime += sum(travel[:i])
                print(totalTime, sum(travel[:i]), travel[:i], "G")
                flagG = True
            if "P" in garbage[i] and not flagP:
                totalTime += sum(travel[:i])
                print(totalTime, sum(travel[:i]), travel[:i], "P")
                flagP = True
            if "M" in garbage[i] and not flagM:
                totalTime += sum(travel[:i])
                print(totalTime, sum(travel[:i]), travel[:i], "M")
                flagM = True
        
        return totalTime

solution = Solution()
garbage = ["G","P","GP", "GG"]
travel = [2,4,3]
result = solution.garbageCollection(garbage, travel)
print(result)
        