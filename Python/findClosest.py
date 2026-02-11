class Solution:
    def length(self, val: int, val2: int):
        length = 0
        for i in range(val, val2):
            length += 1
        return length

    def findClosest(self, x: int, y: int, z: int) -> int:
        xLength = 0
        yLength = 0
    
        if(x < z):
            xLength = self.length(x, z)
        else:
            xLength = self.length(z, x)

        if(y < z):
            yLength = self.length(y, z)
        else:
            yLength = self.length(z, y)
    
        if(xLength < yLength):
            return 1
        elif(xLength == yLength):
            return 0
        else:
            return 2


solution = Solution()
x = 2
y = 7
z = 4
result = solution.findClosest(x, y, z)
print(result)