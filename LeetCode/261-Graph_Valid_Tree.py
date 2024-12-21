class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        node_map = { i:[] for i in range(n) }

        for start, finish in edges:
            node_map[start].append(finish)
            node_map[finish].append(start)

        visited = set()

        def has_cycle(node, prevNode):
            if node in visited:
                return True
            
            visited.add(node)

            for neighbour in node_map[node]:
                if neighbour != prevNode and has_cycle(neighbour, node):
                    return True
            
            return False

        return not has_cycle(0, -1) and len(visited) == n
    
# Time Complexity: O(V + E)
# Space Complexity: O(V + E)