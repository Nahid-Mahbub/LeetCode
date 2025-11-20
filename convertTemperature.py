class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        return [celsius + 273.15, celsius * 1.80 + 32.00]

solution = Solution()
celsius = 36.50
result = solution.convertTemperature(celsius)
print(result)