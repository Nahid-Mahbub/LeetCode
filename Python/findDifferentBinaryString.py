class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        length = len(nums[0])
        setNums = set(nums)
        def generate_binary(n, s=""):
            if(len(s) == n):
                if (s not in setNums):
                    return s
                return
            ans = generate_binary(n, s + "0")
            if ans:
                return ans
            ans = generate_binary(n, s + "1")
            if ans:
                return ans
        return generate_binary(length)
    
solution = Solution()
nums = ["01","10"]
result = solution.findDifferentBinaryString(nums)
print(result)