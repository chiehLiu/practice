# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        # Time: O(n)
        # Space: O(1)
        
        # find the middle of the list
        # in the end the slow will be the middle and fast will be the end
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
          
        # reverse the second half of the list
        # this reverse func is happened in the middle of the list, 
        # so the list would be divided into two halves
        # first is the ascending order, second is the reversed one
        # 1 -> 2 -> 3 -> 4 -> 5

        # 1 -> 2 -> 3 = first
        # 5 -> 4 = second
        pre, curr = None, slow
        while curr:
            nxt = curr.next
            curr.next = pre
            pre = curr
            curr = nxt
        
        # merge the two halves
        first, second = head, pre
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next