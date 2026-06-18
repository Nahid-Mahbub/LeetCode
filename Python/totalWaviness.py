class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        if (len(str(num2)) < 3):
            return 0
        counter = 0
        for i in range(num1, num2+1):

            listNum = [int(d) for d in str(i)]
            for j in range(1, len(listNum)-1, 1):
                if (listNum[j-1] < listNum[j] and listNum[j] > listNum[j+1]):
                    counter += 1
                    print(i)
                    continue

                elif(listNum[j-1] > listNum[j] and listNum[j] < listNum[j+1]):
                    counter += 1
                    print(i)
                    continue
        return counter


solution = Solution()
num1 = 198
num2 = 202
result = solution.totalWaviness(num1, num2)
print(result)