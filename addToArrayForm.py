class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        sys.set_int_max_str_digits(100000)
        num = int("".join(map(str, num)))
        num += k
        return list(map(int, str(num)))

solution = Solution()
num = [2,7,4]
k = 181
result = solution.addToArrayForm(num, k)
print(result)
