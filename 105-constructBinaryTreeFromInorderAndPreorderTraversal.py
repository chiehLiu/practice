# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# In Python, when solving a problem like LeetCode 105 
# (“Construct Binary Tree from Preorder and Inorder Traversal”), 
# if the output is represented as [3,9,20,null,null,15,7], the null values in the output correspond to None.

# so the preorder traversal is go root -> left -> right
# using the preorder traversal, we can find the root of the tree or any subtree(the first one would be the root)
# and the inorder traversal is go left -> root -> right
# since we have the root from the preorder traversal, we can differentiate the left and right node from a tree or subtree.

# time complexity: O(n)
# space complexity: O(n)

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root

