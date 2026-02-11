class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        answer = 0
        temp = 10**18
        nums.sort()
        for i in range(len(nums)):
            if(i > 0 and nums[i] == nums[i-1]):
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                numSum = nums[i] + nums[left] + nums[right]
                print(numSum)
                if(numSum == target):
                    return target
                elif(numSum > target):
                    right -= 1
                elif(numSum < target):
                    left += 1
                if(numSum > target):
                    if(numSum - target < temp):
                        temp = numSum - target
                        answer = numSum
                else:
                    if(target - numSum < temp):
                        temp = target - numSum
                        answer = numSum
        return answer
solution = Solution()
nums = [-1,2,1,-4]
target = 1
result = solution.threeSumClosest(nums, target)
print(result)