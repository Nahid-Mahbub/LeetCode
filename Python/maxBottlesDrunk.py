class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        
        fullBottles = numBottles
        emptyBottles = 0
        bottlesDrunk = 0
        while fullBottles > 0:
            bottlesDrunk += fullBottles
            emptyBottles += fullBottles
            fullBottles = 0
            if(emptyBottles - numExchange >= 0):
                fullBottles += 1
                emptyBottles -= numExchange
                numExchange += 1
            else:
                break
        return bottlesDrunk
    
solution = Solution()
numBottles = 10
numExchange = 3
resunlt = solution.maxBottlesDrunk(numBottles, numExchange)
print(resunlt)