# Union Find
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            res = n1

            while res != par[res]:
                # optimization, setting the parent to grandparent
                par[res] = par[par[res]] 

                res = par[res]
    
            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0
            
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]

            return 1
        
        res = n
        
        for n1, n2 in edges:
            res -= union(n1, n2)

        return res

# Regular approach
# class Solution:
#     def countComponents(self, n: int, edges: List[List[int]]) -> int:
#         nodeMap = { i:[] for i in range(n) }
#         counter = 0
#         visited = [0 for i in range(n)]

#         for node1, node2 in edges:
#             nodeMap[node1].append(node2)
#             nodeMap[node2].append(node1)

#         def dfs(node):
#             if visited[node]:
#                 return

#             visited[node] = 1
            
#             for neighbour in nodeMap[node]:
#                 dfs(neighbour)
        
#         for node in range(n):
#             if not visited[node]:
#                 counter += 1
#                 dfs(node)

#         return counter
    
# Time Complexity: O(V + E)
# Space Complexity: O(V + E)