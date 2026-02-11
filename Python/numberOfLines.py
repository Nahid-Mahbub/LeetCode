class Solution:
    def numberOfLines(self, widths: list[int], s: str) -> list[int]:
        myDic = {}
        counter = 0
        lineCounter = 1
        for i in range(len(widths)):
            myDic[chr(97 + i)] = widths[i]
        for char in s:
            counter += myDic[char]
            if(counter == 100):
                lineCounter += 1
                if(char != s[len(s) - 1]):
                    counter = 0
                else:
                    lineCounter -= 1
            elif(counter > 100):
                lineCounter += 1
                counter = myDic[char]
        return [lineCounter, counter]
solution = Solution()
widths = [3,4,10,4,8,7,3,3,4,9,8,2,9,6,2,8,4,9,9,10,2,4,9,10,8,2]
s = "mqblbtpvicqhbrejb"
result = solution.numberOfLines(widths, s)
print(result)