class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max_wealth = 0
        for i in range(len(accounts)):
            count = 0
            for j in range(len(accounts[i])):
                count += accounts[i][j]
            if (count > max_wealth):
                max_wealth = count
        return max_wealth

solution = Solution()
accounts = [[1,2,3],[3,2,1]]
result = solution.maximumWealth(accounts)
print(result)