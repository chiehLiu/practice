# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time: O(n)
# Space: O(h) h is the height of the tree

# thinking process:

# first setup the res:
# since we need to mutate the res inside the dfs, so we choose the list as our res, 
# in this way, we don't have to worry about the variable mutation issue.

# second:
# I will call the dfs, and pass the root

# third:
# return the res[0]

# fourth:
# implement the dfs
# thinking of dfs, the return condition would be if the node pass in was None, return 0,
# meaning the traversal reaching the end of the tree

# right now the base setup for this problem is done.

# ------------------------------------------------------------------------------------------------------------

# dfs:
# 1.
# we need to go to the end fo the tree
# so we call dfs and pass in the left node and right node

# 2.
# there would be negative value, so we compare it with 0

# 3.
# update the res
# at this line of code meaning we are at the split of the tree node,
# so we have to update the current path to res, to make sure we get the max path sum
# because the path sum does not need to go through the root node

# 4.
# after the update.
# we could return the max path sum of the current node either left or right
# because a path can not go both left and right, so we return the bigger one plus the current node value

# so we keep update the res with the leftMax + rightMax + node.val and return the one bigger side of the tree
# till the root node.

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(node):
            if not node:
                return 0
            
            leftMax = dfs(node.left)
            rightMax = dfs(node.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            res[0] = max(res[0], node.val + leftMax + rightMax)

            return node.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]