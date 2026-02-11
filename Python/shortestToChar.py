class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        counts = []
        answer = []
        for i in range(len(s)):
            if(c == s[i]):
                counts.append(i)
        print(counts)
        for i in range(len(s)):
            val = float('inf') #Max value float('inf')
            for count in counts:
                print("Count = ", count, i)
                distance = abs(count - i) #abs() always possitive values
                if(distance < val):
                    val = distance
                    print(distance, count, i)
            answer.append(val)
        return answer

solution = Solution()
s = "loveleetcode"
c = "e"
result = solution.shortestToChar(s, c)
print(result)