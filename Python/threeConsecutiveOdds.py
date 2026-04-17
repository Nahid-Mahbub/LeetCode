class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        counter = 0
        for num in arr:
            if (num % 2 != 0):
                counter += 1
            else:
                counter = 0
            if (counter == 3):
                return True
        return False
        
solution = Solution()
arr = [1,2,34,3,4,5,7,23,12]
result = solution.threeConsecutiveOdds(arr)
print(result)