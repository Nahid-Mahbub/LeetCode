class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:        
        set_b = set()
        common = 0
        output = []
        for i in range(len(A)):
            set_b.add(B[i])
            for j in range(i+1):
                if A[j] in set_b:
                    common += 1
            output.append(common)
            common = 0
        return output
solution = Solution()
A = [2,3,1]
B = [3,1,2]
result = solution.findThePrefixCommonArray(A, B)
print(result)