class Solution(object):
    # O(n) time complexity
    # O(1) space complexity
    
    # in order to find the largest sum from  subArray, we need to keep track of the curr_sum and max_sum
    # we will iterate through the array and keep track of the current sum
    # if the current sum is greater than the current element, we will keep the current sum
    # if the current sum is less than the current element, we will keep the current element
    # we will also keep track of the max sum
    # if the current sum is greater than the max sum, we will keep the current sum
    # if the max sum is greater than the current sum, we will keep the max sum
    # return the max sum
    
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = float("-inf")
        cur_sum = 0

        for num in nums:
            cur_sum = cur_sum + num
            cur_sum = max(num, cur_sum)
            max_sum = max(cur_sum, max_sum)

        return max_sum