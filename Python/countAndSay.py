class Solution:
    def countAndSay(self, n: int) -> str:
        output = "1"
        for _ in range(n-1):
            temp = []
            counter = 1
            for i in range(1, len(output)):            
                if(output[i] == output[i-1]):
                    counter += 1
                else:
                    temp.append(str(counter))
                    temp.append(output[i - 1])
                    counter = 1
            
            temp.append(str(counter))
            temp.append(output[-1])
            output = "".join(temp)
        return output
    
solution = Solution()
n = 1
result = solution.countAndSay(n)
print(result)