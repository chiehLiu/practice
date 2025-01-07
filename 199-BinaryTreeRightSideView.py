# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# it's basically the same as 102, but we only need the rightmost ele of each level
# BFS

# TIme: O(n), n is the number of nodes in the tree
# Space: O(w), w is the number of widest level in the tree

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = collections.deque()

        q.append(root)

        res = []

        while q:
            qLen = len(q)
            level = []
            
            for i in range(qLen):
                node = q.popleft()

                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            if level:
                rightEle = level.pop()
                res.append(rightEle)
        
        return res

