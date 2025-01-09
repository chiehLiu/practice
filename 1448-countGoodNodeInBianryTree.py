# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        max_val = float("-inf")

        def dfs(curr, max_val):
            if not curr:
                return
            
            if curr.val >= max_val:
                self.res += 1
                max_val = max(max_val, curr.val)

            dfs(curr.left, max_val)
            dfs(curr.right, max_val)
        
        dfs(root, max_val)

        return self.res