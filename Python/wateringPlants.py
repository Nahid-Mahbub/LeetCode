class Solution:
    def wateringPlants(self, plants: list[int], capacity: int) -> int:
        steps = 0
        currentCapacity = capacity
        for i in range(len(plants)):
            if plants[i] > currentCapacity:
                steps += 2 * i
                currentCapacity = capacity

            steps += 1
            currentCapacity -= plants[i]
        return steps

solution = Solution()
plants = [2, 2, 3, 3]
capacity = 5
result = solution.wateringPlants(plants, capacity)
print(result)