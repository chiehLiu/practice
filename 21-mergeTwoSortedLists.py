# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Time: O(n), n is the total number of nodes in list1 and list2
    # Space: O(1), if we need to count the output, it will be O(n). but we don't need to count the output typically

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # the reason we need two variables here
        # is because one for return the result
        # the other one iterating through the list
        dummy = node = ListNode()

        # both list have values
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            # after we attach the smaller value, we move the node to the next
            node = node.next
        
        # if one of the list is empty or run out of values
        # we simply attach the rest of it to the result
        node.next = list1 or list2

        # return dummy.next
        # if we return dummy, it will return the initial value which is 0, and it's not in list1 and list2
        return dummy.next