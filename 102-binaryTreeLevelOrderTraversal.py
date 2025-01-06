# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS
# Time: O(n), n is the number of nodes in the tree
# Space: O(n), n is the number of nodes in the tree

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # tree is empty
        if not root:
            return []
        
        # tree at least has one node
        res = []

        q = collections.deque()

        # init the queue
        q.append(root)

        while q:
            qLen = len(q)

            # empty the level
            level = []

            # loop through the current level
            for i in range(qLen):
                # pop the leftmost node
                node = q.popleft()
                
                # if the node it not None, add it to the level
                # and add its children to the queue, in order to process them in the next iteration
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            # empty check, make sure we are not adding empty levels
            if level:
                res.append(level)
        
        return res
