"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodes_dict = {}

        def dfs(cur):
            if not cur:
                return
            
            print(cur.val)
            new_node = Node(cur.val, [])
            nodes_dict[cur.val] = new_node

            for neighbour in cur.neighbors:
                if neighbour.val in nodes_dict.keys():
                    new_node.neighbors.append(nodes_dict[neighbour.val])
                else:
                    new_neighbour = dfs(neighbour)
                    new_node.neighbors.append(new_neighbour)
            
            return new_node

        return dfs(node)
    
# Time Complexity: O(V + E)
# Space Complexity: O(V)