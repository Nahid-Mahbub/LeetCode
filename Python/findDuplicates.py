class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        if (len(nums) == len(set(nums))):
            return []
        
        result = []
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        print(freq)
        for num in freq:
            if (freq[num] > 1):
                result.append(num)
        result.sort()
        return result
    
solution = Solution()
nums = [4,3,2,7,8,2,3,1]
result = solution.findDuplicates(nums)
print(result)