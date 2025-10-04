class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        new_list = []
        for i in range(n):
            new_list.append(nums[i])
            new_list.append(nums[n+i])
        return new_list
solution = Solution()
nums = [2,5,1,3,4,7]
n = 3
result = solution.shuffle(nums, n)
print(result)