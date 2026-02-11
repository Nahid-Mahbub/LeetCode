class Solution:
    def smallestNumber(self, pattern: str) -> str:
        output = ""
        temp = ""
        n = len(pattern)

        for i in range(n + 1):
            # If we reached the end, flush remaining temp
            if i == n:
                temp += str(i + 1)
                output += temp[::-1]
                break

            temp += str(i + 1)

            if pattern[i] == "I":
                output += temp[::-1]
                temp = ""

        return output


    
solution = Solution()
pattern = "IIIDIDDD"
result = solution.smallestNumber(pattern)
print(result)