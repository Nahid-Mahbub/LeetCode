class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # for i in range(len(numbers)):
        #     value = target - numbers[i]
        #     temp = numbers[i]
        #     numbers[i] = "_"
        #     if(value in numbers and numbers.index(value) != i):
        #         print(i, numbers.index(value))
        #         return [i+1, (numbers.index(value) + 1)]
        #     numbers[i] = temp
        # Solve 2
        sorted(numbers)
        left = 0
        right = len(numbers) - 1
        while left < right:
            numSum = numbers[left] + numbers[right]
            if(numSum == target):
                return [left+1, right+1]
            elif(numSum < target):
                left += 1
            elif(numSum > target):
                right -= 1
    
solution = Solution()
numbers = [1,2,3,4,4,9,56,90]
target = 8
result = solution.twoSum(numbers, target)
print(result)