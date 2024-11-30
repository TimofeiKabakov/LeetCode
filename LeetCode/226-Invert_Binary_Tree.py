# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def invert_recursive(root):
    if not root:
        return

    root.left, root.right = root.right, root.left

    invert_recursive(root.left)
    invert_recursive(root.right)

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        invert_recursive(root)
        return root