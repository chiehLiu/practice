class Solution:
    # I don't understand this at all. I will come back to this later
    def findDuplicate(self, nums: List[int]) -> int:
        # we should identify the beginning of the cycle, and it would be the duplicate number
        # and here we can use the Floyd's Tortoise and Hare (Cycle Detection) algorithm
        # the idea is to have two pointers, slow and fast. they will meet the first time, and we set the second slow pointer
        # to the beginning, and move them one step at a time, and they will meet at the beginning of the cycle
        # let's prove it here:
        # since 2slow = fast
        # and the distance between the beginning to the cycle is p
        # and the distance between the cycle to the Intersection is x
        # and the distance of the linked list cycle is c
        # and the distance of the linked list cycle without the x is c-x
        # so we have the following equations:
        # 2(p+c-x) = p+c+c-x
        # => 2p+2c-2x = p+2c-x
        # => p = x 
        # so the distance between the beginning to the cycle is equal to the distance between the cycle to the Intersection

        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow