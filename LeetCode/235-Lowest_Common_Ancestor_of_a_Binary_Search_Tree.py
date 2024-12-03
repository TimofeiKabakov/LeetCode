# Working solution but overcomplicated
class Solution:
    def __init__(self):
        self.counter = 0
        self.map = {}

    def dfs(self, node):
        if not node:
            return 0
        self.map[self.counter] = node.val
        node.val = self.counter
        self.counter += 1
        return self.dfs(node.left) + self.dfs(node.right) + 1 

    def find_parents(self, node, parents):
        if not node:
            return
        
        if node.left:
            parents[node.left.val] = node
        if node.right:
            parents[node.right.val] = node
        
        self.find_parents(node.left, parents)
        self.find_parents(node.right, parents)

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = 0
        number_of_elements = self.dfs(root)
        tree_parents = [0] * number_of_elements
        tree_parents[0] = root
        self.find_parents(root, tree_parents)

        set_p = set()
        set_q = set()
        
        while(p != q):
            set_p.add(p.val)
            set_q.add(q.val)
            print("p:", p.val, "q:", q.val)
            if p != root:
                p = tree_parents[p.val]
            if q != root:
                q = tree_parents[q.val]
            
            if q.val in set_p:
                q.val = self.map.get(q.val)
                return q
            if p.val in set_q:
                p.val = self.map.get(p.val)
                return p

        p.val = self.map.get(p.val)
        return p


# Time Complexity: O(n)
# Space Complexity: O(n)