# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# time: O(n)
# space: O(n)

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        cur = root

        # we use or operator to make sure that we are going to iterate all the nodes
        # since the cur would be none in the process(meet the right node is none in the process) 
        # but the stack is not
        while cur or stack:

            # go to the left most node
            # and add all the nodes to the stack
            while cur:
                stack.append(cur)
                cur = cur.left
            
            # pop the last node from the stack
            # and check if it is the kth smallest
            cur = stack.pop()

            k -= 1
            if k == 0:
                return cur.val
            
            # go to the right node
            cur = cur.right
        