class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        answer = []
        phone = {
        "2": "abc", "3": "def", "4": "ghi",
        "5": "jkl", "6": "mno", "7": "pqrs",
        "8": "tuv", "9": "wxyz"
        }

        def recursion(i, path):
            if(i == len(digits)):
                answer.append("".join(path))
                return
            for char in phone[digits[i]]:
                path.append(char)
                recursion(i+1, path)
                path.pop()
        recursion(0, [])
        return answer


solution = Solution()
digits = "23"
result = solution.letterCombinations(digits)
print(result)