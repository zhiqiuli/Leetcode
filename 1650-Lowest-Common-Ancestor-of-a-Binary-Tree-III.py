"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

"""
METHOD 1
"""
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        path = set()
        while p:
            path.add(p)
            p = p.parent
        while q not in path:
            q = q.parent
        return q

"""
METHOD 2
"""
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_depth = self.get_depth(p)
        q_depth = self.get_depth(q)
        
        if p_depth > q_depth:
            diff = p_depth - q_depth
            for _ in range(diff):
                p = p.parent

        if p_depth < q_depth:
            diff = q_depth - p_depth
            for _ in range(diff):
                q = q.parent
        
        while p != q:
            p = p.parent
            q = q.parent
            
        return p
                
    def get_depth(self, node):
        depth = 0
        while node:
            depth += 1
            node = node.parent
        return depth

"""
METHOD 3
"""
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        root = p
        while root:
            if root.parent is None:
                break
            root = root.parent
        return self.dfs(root, p, q)
        
    def dfs(self, root, p, q):
        
        if root is None:
            return None
        
        if root.val == p.val or root.val == q.val:
            return root
        
        lca_left  = self.dfs(root.left , p, q)
        lca_right = self.dfs(root.right, p, q)
        
        if lca_left and lca_right:
            return root
        
        if lca_left and not lca_right:
            return lca_left
        
        if not lca_left and lca_right:
            return lca_right
