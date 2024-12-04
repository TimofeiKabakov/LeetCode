class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node:
                return None

            if (p.val < node.val and q.val > node.val) or (q.val < node.val and p.val > node.val):
                return node
            elif p.val == node.val:
                return p
            elif q.val == node.val:
                return q

            return dfs(node.left) if p.val < node.val and q.val < node.val else dfs(node.right)

        return dfs(root)

# Time Complexity: O(log n)
# Space Complexity: O(1)