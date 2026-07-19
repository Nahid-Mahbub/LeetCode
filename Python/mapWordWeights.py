class Solution:
    def mapWordWeights(self, words: list[str], weights: list[int]) -> str:
        result = ""

        weightsDic = {}
        val = ord('a')

        for weight in weights:
            weightsDic[chr(val)] = weight
            val += 1

        reverseWeights = {}

        for i in range(26):
            reverseWeights[i] = chr(ord('z') - i)

        for word in words:
            sumWords = 0
            for char in word:
                sumWords += weightsDic[char]

            result += reverseWeights[sumWords % 26]

        return result
solution = Solution()
words = ["abcd"]
weights = [7,5,3,4,3,5,4,9,4,2,2,7,10,2,5,10,6,1,2,2,4,1,3,4,4,5]
result = solution.mapWordWeights(words, weights)
print(result)
