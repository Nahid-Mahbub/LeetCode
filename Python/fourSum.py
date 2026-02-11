class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        answer = []
        nums.sort()
        for i in range(len(nums)):
            if(i > 0 and nums[i] == nums[i-1]):
                continue
            print("Loop_1:", nums[i], i)
            for j in range(i+1, len(nums)):
                if(j-1 != i and nums[j] == nums[j-1]):
                    continue
                print("Loop_2:", nums[j], j)
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    numSum = nums[i] + nums[j] + nums[left] + nums[right]
                    if(numSum == target):
                        answer.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif(numSum > target):
                        right -= 1
                    elif(numSum < target):
                        left += 1
                    print("Loop_3:", nums[left], nums[right], left, right)
                    print(numSum)
        return answer
solution = Solution()
nums = [2, 2, 2, 2, 2] #1,0,-1,0,-2,2
target = 8
result = solution.fourSum(nums, target)
print(result)
