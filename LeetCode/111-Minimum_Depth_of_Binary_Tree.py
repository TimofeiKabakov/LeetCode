# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, node: Optional[TreeNode]) -> int:
        if(node is None):
            return 0

        if(not node.left and not node.right):
            return 1

        if(node.left and node.right):
            return min(self.minDepth(node.left), self.minDepth(node.right)) + 1
        elif(node.left):
            return self.minDepth(node.left) + 1
        else:
            return self.minDepth(node.right) + 1