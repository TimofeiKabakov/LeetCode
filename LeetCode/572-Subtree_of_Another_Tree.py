def same_tree(node1, node2) -> bool:
    if not node1 and not node2:
        return True
    if not node1 or not node2:
        return False

    return node1.val == node2.val and same_tree(node1.left, node2.left) and same_tree(node1.right, node2.right)

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        return same_tree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)