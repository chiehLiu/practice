# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time: O(n*m) where n is the number of nodes in the root and m is the number of nodes in the subRoot
# Space: O(m+n) where n is the number of nodes in the root and m is the number of nodes in the subRoot
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # one of them are empty
        if not subRoot: return True
        if not root: return False

        # check the root itself and subRoot are the same
        # both empty situation will be checked here
        if self.sameTree(root, subRoot):
            return True
        
        # check root child and subRoot are the same
        # both tree have val
        return (self.isSubtree(root.left, subRoot) or 
            self.isSubtree(root.right, subRoot))

    
    def sameTree(self, r, s):
        # they both empty so they are the same
        if not r and not s:
            return True
        
        # both of them have val and equal
        if r and s and r.val == s.val:
            return (self.sameTree(r.left, s.left) and
                self.sameTree(r.right, s.right))

        # one of them have val
        return False
        

