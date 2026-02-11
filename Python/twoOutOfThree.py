class Solution:
    def twoOutOfThree(self, nums1: list[int], nums2: list[int], nums3: list[int]) -> list[int]:
        nums_set = set()
        for num in nums3:
            if(num in nums2 or num in nums1):
                print(num)
                nums_set.add(num)
        for num in nums2:
            if(num in nums1 or num in nums3):
                print(num)
                nums_set.add(num)
        return list(nums_set)

solution = Solution()
nums1 = [1,2,2]
nums2 = [4,3,3]
nums3 = [5]
result = solution.twoOutOfThree(nums1, nums2, nums3)
print(result)