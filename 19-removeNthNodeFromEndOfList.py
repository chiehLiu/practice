# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Time Complexity: O(L) where L is the length of the linked list.
    # Space Complexity: O(1)

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy

        # Move the fast pointer n + 1 steps ahead. We move it n + 1 steps instead of n so that the slow pointer will land on the node just before the one we want to remove.
        # so that we can remove the node after the slow pointer.
        for _ in range(n + 1):
            fast = fast.next
        
        # Move the fast pointer to the end, maintaining the gap.
        while fast:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next

        return dummy.next