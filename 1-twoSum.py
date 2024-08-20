class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ## 1. brute force solution
        # Time complexity: O(n^2)
        # Space complexity: O(1)
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # ------------------------------------------------

        ## 2. hash table solution
        # Time complexity: O(n)
        # Space complexity: O(n)
        hash_table = {}

        # enumerate func get the index and the value of the list
        # hash_table is a dictionary, key is the number, the value is the index
        for i, number in range(enumerate(nums)):
            if target - number in hash_table:
                return [hash_table[target - number], i]
            else:
                hash_table[number] = i

        # ------------------------------------------------

        ## 3. two pointer solution
        # the condition is list should be sorted
        # Time complexity: O(nlogn)
        # Space complexity: O(n)

        # Pair each number with its original index
        # (num, i) here is like a schema of the list
        nums_with_indices = [(num, i) for i, num in enumerate(nums)]
        
        # Sort based on the numbers
        nums_with_indices.sort()

        left, right = 0, len(nums_with_indices) - 1
        while left < right:
            current_sum = nums_with_indices[left][0] + nums_with_indices[right][0]
            if current_sum == target:
                return [nums_with_indices[left][1], nums_with_indices[right][1]]
            elif current_sum < target:
                left += 1
            else:
                right -= 1