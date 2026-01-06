class Solution:
    def recoverOrder(self, order: list[int], friends: list[int]) -> list[int]:
        output = []
        for num in order:
            if(num in friends):
                output.append(num)
        return output
    
solution = Solution()
order = [3,1,2,5,4]
friends = [1,3,4]
result = solution.recoverOrder(order, friends)
print(result)