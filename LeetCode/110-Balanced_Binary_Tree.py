def height(root):
    if not root:
        return 0

    return max(height(root.left), height(root.right)) + 1

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        left_sub = height(root.left)
        right_sub = height(root.right)

        if abs(left_sub - right_sub) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)


# Another Solution:
# class Solution:
#     def isBalanced(self, root: Optional[TreeNode]) -> bool:
#         self.max_diff = 0

#         def dfs(root):
#             if not root:
#                 return 0

#             left_sub = dfs(root.left)
#             right_sub = dfs(root.right)

#             self.max_diff = max(self.max_diff, abs(left_sub - right_sub))

#             return max(left_sub, right_sub) + 1

#         dfs(root)

#         return self.max_diff <= 1