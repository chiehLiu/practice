class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # "Product" is a mathematical term that specifically refers to the result of multiplying numbers together.
        # For example, the product of the numbers 2, 3, and 4 is 2×3×4=24.
        
        length = len(nums)
        
        # Initialize the answer array with 1s.
        answer = [1] * length
        
        # Calculate the products of all elements to the left of each element.
        left_product = 1
        for i in range(length):
            answer[i] = left_product
            left_product *= nums[i]
        
        # Calculate the products of all elements to the right of each element.
        right_product = 1
        for i in range(length - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]
        
        return answer
