class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        answer = []
        for i in range(left, right+1):
            chars = str(i)
            flag = 0
            for char in chars:
                value = int(char)
                if(value == 0 or i % value != 0):
                    flag = 1
                    break
            if(flag == 0):
                answer.append(i)
        return answer

solution = Solution()
left = 1
right = 22
result = solution.selfDividingNumbers(left, right)
print(result)