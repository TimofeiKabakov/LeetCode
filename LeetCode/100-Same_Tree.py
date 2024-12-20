class Solution:
    def isSameTree(self, node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False

        return node1.val == node2.val and self.isSameTree(node1.left, node2.left) and self.isSameTree(node1.right, node2.right)