class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        counter = 0
        for op in operations:
            if(op == "--X"):
                counter -= 1
            elif(op == "X++"):
                counter += 1
            elif(op == "++X"):
                counter += 1
            elif(op == "X--"):
                counter -= 1
        return counter

solution = Solution()
operations = ["X++","++X","--X","X--"]
result = solution.finalValueAfterOperations(operations)
print(result)