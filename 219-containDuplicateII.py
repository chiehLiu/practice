class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        l, r = 0, 0

        window = set()

        while r < len(nums):

            if r - l > k:
                window.remove(nums[l])
                l += 1

            if nums[r] in window:
                return True
            else:
                window.add(nums[r])
                r += 1
        
        return False
  

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        L = 0
        window = set()

        for R in range(len(nums)):
            if R - L > k:
                window.remove(nums[L])
                L += 1
            
            if nums[R] in window:
                return True
            
            window.add(nums[R])
            
        return False
        