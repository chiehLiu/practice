class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ## 1. brute force solution
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # ------------------------------------------------

        ## 2. hash table solution
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

        # nums.sort() so we sorted the list to demo the case


        # left, right = 0, len(nums) - 1
        # while left < right:
        #     if nums[left] + nums[right] == target:
        #         return [left, right]
        #     elif nums[left] + nums[right] < target:
        #         left += 1
        #     else:
        #         right -= 1