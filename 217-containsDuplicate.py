class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        # 1. Brute force solution
        # Time complexity: O(n^2)
        # Space complexity: O(1)
        #
        # for i in range(len(nums)):
        #   for j in range(i+1, len(nums)):
        #     if nums[i] == nums[j]:
        #       return True
        # return False
        
        # ------------------------------------------------
        
        
        # 2. Hash table solution
        # Time complexity: O(n)
        # Space complexity: O(n)
        
        # hash_table = {}
        # for num in nums:
        #     if num in hash_table:
        #       return True
        #     else:
        #       hash_table[num] = 1
              
        # return False
        
        
        # ------------------------------------------------
        
        # 3. Sorting solution
        # compare the current element with the previous element

        # Time complexity: O(nlogn)
        # Space complexity: O(n)

        # nums.sort() so the list would be like [1, 1, 2, 3, 4, 5]
        
        # then compare the current element with the previous element
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return True

        # return False
        
        # ------------------------------------------------
        
        # 4. Set solution
        # Set is a collection of unique elements 
        # so if the length of the set is not equal to the length of the list, there are duplicates
        # Time complexity: O(n)
        # Space complexity: O(n)
        
        return True if len(set(nums)) != len(nums) else False