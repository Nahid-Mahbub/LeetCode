class Solution:
    def findComplement(self, num: int) -> int:
        binary = list(bin(num))
        for i in range(2, len(binary)):
            if(binary[i] == "0"):
                binary[i] = "1"
            else:
                binary[i] = "0"
        invertedBinary = "".join(binary[2:])
        return int(invertedBinary, 2)
    
solution = Solution()
num = 5
result = solution.findComplement(num)
print(result)