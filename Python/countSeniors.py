class Solution:
    def countSeniors(self, details: list[str]) -> int:
        counter = 0
        for age in details:
            if(int(age[11:13:1]) > 60):
                counter += 1
        return counter
    
solution = Solution()
details = ["7868190130M7522","5303914400F9211","9273338290F4010"]
result = solution.countSeniors(details)
print(result)