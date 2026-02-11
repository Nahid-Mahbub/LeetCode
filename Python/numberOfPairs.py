class Solution:
    def numberOfPairs(self, nums1: list[int], nums2: list[int], k: int) -> int:
        counter = 0
        for num1 in nums1:
            for num2 in nums2:
                if(num1 % (num2 * k) == 0):
                    counter += 1
        return counter

solution = Solution()
nums1 = [1,3,4]
nums2 = [1,3,4]
k = 1
result = solution.numberOfPairs(nums1, nums2, k)
print(result)