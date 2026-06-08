class Solution:
    def customSortString(self, order: str, s: str) -> str:
        stringCount = {
            'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0,
            'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0,
            'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0,
            'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0,
            'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0,
            'z': 0
        }
        result = []
        for char in s:
            stringCount[char] += 1

        for char in order:
            if stringCount[char] > 0:
                result.append(char * stringCount[char])
                stringCount[char] = 0
        for char in stringCount:
            if stringCount[char] > 0:
                result.append(char * stringCount[char])

        return "".join(result)
    
solution = Solution()
order = "cba"
s = "abcd"
result = solution.customSortString(order, s)
print(result)