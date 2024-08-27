# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev, curr = None, head

        # Approach 1: Iterative
        # Time complexity: O(n)
        # Space complexity: O(1)

        # curr would be None when we reach the end of the list
        while curr:
            
            # save the next node
            nxt = curr.next

            # reverse the current node
            curr.next = prev

            # move prev and curr one step forward
            prev = curr
            curr = nxt

        return prev
    
    # Recursive solution

    # def reverseList(self, head):
    #     # Base case: If head is None or only one node, it's already reversed.
    #     if head is None or head.next is None:
    #         return head
        
    #     # Recursive step: reverse the rest of the list.
    #     reversed_head = self.reverseList(head.next)
        
    #     # Reverse the current node.
    #     head.next.next = head
    #     head.next = None
        
    #     return reversed_head

# Time complexity: O(n)
# Space complexity: O(n) due to the recursive stack

# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/description/
# Approach 1: Iterative
# Approach 2: Recursive