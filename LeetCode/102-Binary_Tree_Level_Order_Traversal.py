# BFS Solution
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        level = 0
        queue = collections.deque([root])

        while queue:
            length_q = len(queue)
            sub_level = []
            for i in range(length_q):
                node = queue.popleft()
                if node:
                    sub_level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            
            if len(sub_level):
                res.append(sub_level)

        return res


# DFS solution
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_dict = defaultdict(list)
        
        def dfs(node, level):
            if not node:
                return

            level_dict[level].append(node.val)

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)

        result = list(level_dict.values())
        print(result)

        return result
    
# Time Complexity: O(n)
# Space Complexity: O(n)