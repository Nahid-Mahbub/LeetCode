class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        
        key = set()
        for i in range(len(rooms[0])):
            key.add(rooms[0][i])
        
        for i in range(1, len(rooms)):

            if i not in key:
                if(rooms[i] == []):
                    continue
                return False

            for j in range(len(rooms[i])):
                key.add(rooms[i][j])
            
            print(key)
            
        return True

solution = Solution()
rooms = [[1,3],[1,4],[2,3,4,1],[],[4,3,2]]


result = solution.canVisitAllRooms(rooms)
print(result)