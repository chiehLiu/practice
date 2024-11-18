"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# still need to revise the content.
class Solution:
    # time: O(n)
    # space: O(1)

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Step 1: Create interweaved list
        # 1 -> 1' -> 2 -> 2' -> 3 -> 3' -> 4 -> 4' -> 5 -> 5'
        curr = head
        while curr:
            new_node = Node(curr.val)
            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next

        # Step 2: Connect random pointers for copied nodes
        # renew the curr pointer to the head again
        # if the curr random has a value, then update the copied one to the original random's next
        # since the copied node is always next to the original node
        # lastly move the curr pointer to the next node
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # Step 3: Separate original and copied nodes
        new_head = head.next

        # why we create curr_new variable?
        # because we need to move the new_head to the next node
        curr_new = new_head

        while curr_new and curr_new.next:
            curr_new.next = curr_new.next.next
            curr_new = curr_new.next
        
        return new_head