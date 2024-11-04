# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    
    # space complexity: O(m+n) m is the length of l1, n is the length of l2
    # time complexity: O(1)
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # these are few cases
        # 1. there is no carry number so the addition does not exceed 10
        # 2. there is a carry number
        # 3. the length of the two linked list is different
        # 4. the length of the two linked list is the same

        dummy = node = ListNode()
        carry = 0

        while l1 or l2 or carry:

            # if list is empty, it's val will be 0
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # the sum plus carry
            valC = v1 + v2 + carry

            # sum the val, % 10 here meaning we subtract by 10
            val = (valC) % 10

            # update carry, // 10 here meaning we divide by 10 and get the integer
            carry = (valC) // 10

            # assign the val
            node.next = ListNode(val)

            # move to next node
            node = node.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        
        return dummy.next
        
