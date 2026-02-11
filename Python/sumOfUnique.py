class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        if(len(set(nums)) == len(nums)):
            return sum(nums)
        nums.sort()
        print(nums)
        setNums = set(nums)
        temp = nums[0]
        array = set()
        for i in range(1, len(nums)):
            if(temp == nums[i]):
                array.add(temp)
            else:
                temp = nums[i]
        for num in array:
            setNums.remove(num)
        return sum(setNums)
    
solution = Solution()
nums = [85,83,62,70,5,90,57,21,7,61,97,7,26,32,21,13,5,18]
result = solution.sumOfUnique(nums)
print(result)       