# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if(not root):
            return 0

        def maxDepth(node: Optional[TreeNode]) -> int:
            if(not node):
                return 0
            
            return max(maxDepth(node.left), maxDepth(node.right)) + 1

        left = 0
        right = 0

        if(root.left):
            left = maxDepth(root.left)

        if(root.right):
            right = maxDepth(root.right) 

        return max(left + right, max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right)))