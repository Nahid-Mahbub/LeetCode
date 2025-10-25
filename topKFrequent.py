class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        my_dic = {}
        nums_set = set(nums)
        print(nums_set)
        for num in nums_set:
            counter = 0
            for i in range(len(nums)):
                if(nums[i] == num):
                    counter += 1
            my_dic[num] = counter
        sorted_my_dic = dict(sorted(my_dic.items(), key = lambda item: item[1], reverse = True)[:k])
        print(sorted_my_dic)
        return list(sorted_my_dic.keys())

solution = Solution()
nums = [4,1,-1,2,-1,2,3]
k = 2
result = solution.topKFrequent(nums, k)
print(result)