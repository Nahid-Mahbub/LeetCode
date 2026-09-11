class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:

        dic_edges = {}
        for i in range(len(edges)):
            dic_edges[edges[i][0]] = dic_edges.get(edges[i][0], 0) + 1
            dic_edges[edges[i][1]] = dic_edges.get(edges[i][1], 0) + 1
        print(dic_edges)
       
        return max(dic_edges, key=dic_edges.get)
    
solution = Solution()
edges = [[1,2],[5,1],[1,3],[1,4]]
result = solution.findCenter(edges)
print(result)