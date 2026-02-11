class Solution:
    def convertDateToBinary(self, date: str) -> str:
        print(date)
        date_list = date.split("-")
        for i in range(3):
            date_list[i] = bin(int(date_list[i]))[2::]
        print(date_list)
        return "-".join(date_list)

solution = Solution()
date = "2080-02-29"
result = solution.convertDateToBinary(date)
print(result)
