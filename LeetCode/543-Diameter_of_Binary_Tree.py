class Solution:
    # Proper Solution
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maximum_diameter = 0

        def dfs(root):
            if not root:
                return 0

            length_left = dfs(root.left)
            length_right = dfs(root.right)

            self.maximum_diameter = max(self.maximum_diameter, length_left + length_right)

            return max(length_left, length_right) + 1
        
        dfs(root)

        return self.maximum_diameter



# Another Solution:
# def height_tree(root: Optional[TreeNode]) -> int:
#     if not root:
#         return 0
#     return max(height_tree(root.left), height_tree(root.right)) + 1

# class Solution:
#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0

#         passing_diameter = height_tree(root.left) + height_tree(root.right)
#         max_children = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))

#         return max(passing_diameter, max_children)
        