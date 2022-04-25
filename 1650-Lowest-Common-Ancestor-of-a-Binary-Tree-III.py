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
        p_list = []
        while p:
            p_list.append(p)
            p = p.parent
        q_list = []
        while q:
            q_list.append(q)
            q = q.parent
        if p_list[-1].val != q_list[-1].val:
            return root
        prev = p_list[-1]
        i, j = len(p_list) - 2, len(q_list) - 2
        while i >= 0 and j >= 0:
            if p_list[i].val == q_list[j].val:
                prev = p_list[i]
                i -= 1
                j -= 1
            else:
                return prev
        return prev

"""
METHOD 2
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
