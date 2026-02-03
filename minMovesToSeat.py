class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        seats.sort()
        students.sort()
        counter = 0
        for i in range(len(seats)):
            counter += abs(students[i] - seats[i])

        return counter
    
solutoin = Solution()
seats = [3,1,5]
students = [2,7,4]
result = solutoin.minMovesToSeat(seats, students)
print(result)