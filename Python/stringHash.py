class Solution:
    def stringHash(self, s: str, k: int) -> str:
        value = {
                'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9,
                'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19,
                'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25
            }

        counter = 0
        temp_Value = 0
        result = ""
        for i in range(len(s)):
            counter += 1
            if counter == k:
                temp_Value += value[s[i]]
                result += chr((temp_Value % 26) + ord('a'))
                temp_Value = 0
                counter = 0
            else:
                temp_Value += value[s[i]]
        return result
     
solution = Solution()
s = "abcd"
k = 2
result = solution.stringHash(s, k)
print(result)