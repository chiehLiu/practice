# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # The purpose of the dummy node:
        # It ensures a reference to the start of the list, even if the head changes.
        # It allows the head to be treated like any other node.
        # It simplifies returning the new head of the list after reversal.
        dummy = ListNode(0, head)

        # groupPrev is used to keep track of the node before the current group being reversed.
        groupPrev = dummy

        while True:
            
            # Get the k-th node from groupPrev. This will be the last node in the current group.
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            
            # kth is the next group's prev node
            groupNext = kth.next

            # reverse the group
            prev, curr = groupNext, groupPrev.next
            while curr != groupNext:
                tmp = curr.next  # Temporarily store the next node.
                curr.next = prev  # Reverse the current node's pointer.
                prev = curr  # Move prev to the current node.
                curr = tmp  # Move curr to the next node.
            

            # store the new group starting node
            tmp = groupPrev.next

            # groupPrev.next is updated to point to kth, 
            # which is now the first node of the reversed group.
            groupPrev.next = kth

            # update the groupPrev to the new group starting node
            groupPrev = tmp

        return dummy.next
    
    # this func would return None if the list is shorter than k eventually
    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr 