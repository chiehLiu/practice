# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    
    # Time: O(n)
    # Space: O(1)

    # Floyd's Cycle Detection Algorithm
    # 1. Initialize slow and fast pointers to head
    # 2. Move slow by 1 and fast by 2
    # 3. If slow == fast, then there is a cycle
    # 4. If fast reaches None, then there is no cycle

    # why there would be a cycle?
    # If there is a cycle, then the fast pointer will eventually catch up with the slow pointer
    # If there is no cycle, then the fast pointer will reach the end of the list

    # here is the proof:
    # Let's assume that the cycle has length k
    # When the slow pointer enters the cycle, the fast pointer is already inside the cycle
    # The fast pointer is k steps behind the slow pointer
    # The fast pointer gains 1 step on the slow pointer in each iteration (this the most important part)
    # So, the fast pointer will catch up with the slow pointer after k iterations

    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        fast, slow = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False
    
    # hashSet version is pretty simple but it uses extra space
    # Time: O(n)
    # Space: O(n)
    # def hasCycle(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: bool
    #     """

    #     hashSet = set()
    #     curr = head

    #     while curr:
    #         if curr in hashSet:
    #             return True
    #         hashSet.add(curr)
    #         curr = curr.next

    #     return False