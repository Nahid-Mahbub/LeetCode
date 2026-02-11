class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        counter = 0
        dict = {
            "type": 0,
            "color":  1,
            "name": 2
        }
        for item in items:
            if(item[dict[ruleKey]] == ruleValue):
                counter += 1
        return counter

solution = Solution()
items = [["qqqq","qqqq","qqqq"],["qqqq","qqqq","qqqq"],["qqqq","qqqq","qqqq"],["qqqq","qqqq","qqqq"],["qqqq","qqqq","qqqq"],["qqqq","qqqq","qqqq"],["qqqq","qqqq","qqqq"]]
ruleKey = "name"
ruleValue = "qqqq"
result = solution.countMatches(items, ruleKey, ruleValue)
print(result)