# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# time complexity: O(n*k) not thi fast one
# space complexity: O(1)

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None # since we return the linked list, it should return None when there is no list
        
        # the reason we started from 1 is because we are going to merge the first list with the second list
        for i in range(1, len(lists)):
            # merge the first list with the second list and assign it to the first list
            lists[i] = self.mergeList(lists[i - 1], lists[i])
        
        return lists[-1]
    
    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next