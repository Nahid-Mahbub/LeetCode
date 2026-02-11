class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        positive = []
        negative = []
        output = []
        for num in nums:
            if(num > 0):
                positive.append(num)
            else:
                negative.append(num)
        for i in range(len(positive)):
            output.append(positive[i])
            output.append(negative[i])
        return output

solution = Solution()
nums = [3,1,-2,-5,2,-4]
result = solution.rearrangeArray(nums)
print(result)