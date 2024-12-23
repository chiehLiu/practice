# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.isSame = True
        if not q and not p:
            return True

        def dfs(p, q): 
            if not p and q:
                self.isSame = False
                return
            
            if not q and p:
                self.isSame = False
                return
            
            if not q and not p:
                return

            if p.val != q.val:
                self.isSame = False
                return
            
            dfs(p.left, q.left)
            dfs(p.right, q.right)
            
            
        dfs(p, q)

        return self.isSame