class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        value = ord(target)
        print(value)
        for letter in letters:
            if(value < ord(letter)):
                return letter
        return letters[0]

solution = Solution()
letters = ["c","f","j"]
target = "a"
result = solution.nextGreatestLetter(letters, target)
print(result)