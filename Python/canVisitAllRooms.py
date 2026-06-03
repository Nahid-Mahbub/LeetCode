class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:

        keys = set()
        def dfs(room):
            for key in rooms[room]:
                if key not in keys:
                    keys.add(key)
                    dfs(key) # Recursive call to visit the next room
        keys.add(0)
        dfs(0)
        return len(keys) == len(rooms)


solution = Solution()
rooms = [[1,3],[1,4],[2,3,4,1],[],[4,3,2]]


result = solution.canVisitAllRooms(rooms)
print(result)