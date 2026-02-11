class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        counter = 0
        array = []
        for str in bank:
            if(str.count('1') != 0):
                array.append(str.count('1'))
        for i in range(1, len(array)):
            counter += (array[i-1] * array[i])
        return counter
    
solution = Solution()
bank = ["011001","000000","010100","001000"]
result = solution.numberOfBeams(bank)
print(result)