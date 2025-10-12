class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        ans = set()
        ans2 = set()
        for num in nums1:
            if(num not in nums2):
                ans.add(num)
        for num in nums2:
            if(num not in nums1):
                ans2.add(num)
        ans_list = []
        ans_list.append(list(ans))
        ans_list.append(list(ans2))
        return ans_list

solution = Solution()
nums1 = [1,2,3,3]
nums2 = [1,1,2,2]
result = solution.findDifference(nums1, nums2)
print(result)