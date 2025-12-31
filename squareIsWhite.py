class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        myDic = {
            'a': 1,
            'b': 2,
            'c': 3,
            'd': 4,
            'e': 5,
            'f': 6,
            'g': 7,
            'h': 8
        }
        if((myDic[coordinates[0]] + int(coordinates[1])) % 2 == 0):
            return False
        else:
            return True


solution = Solution()
coordinates = "a1"
result = solution.squareIsWhite(coordinates)
print(result)