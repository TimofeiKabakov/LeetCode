class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacency_list = { i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            adjacency_list[crs].append(pre)

        visited = set()

        def dfs(node):
            if node in visited:
                return False

            visited.add(node)

            for neigbour in adjacency_list[node]:
                if not dfs(neigbour):
                    return False

            visited.remove(node)
            adjacency_list[node] = []

            return True

        for n in range(numCourses):
            if not dfs(n):
                return False
        
        return True
    
# Time Complexity: O(V + E)
# Space Complexity: O(V + E)