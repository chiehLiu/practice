class Solution(object):
    # Time complexity: O(n^2)
    # Space complexity: O(1)

    # Brute force solution
    # For each pair of lines, calculate the area formed by them
    # Keep track of the maximum area
    # Return the maximum area

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0

        for l in range(len(height)):
            for r in range(l + 1, len(height)):
                area = (r - l) * min(height[l], height[r])
                res = max(res, area)
        
        return res
    
class Solution(object):
    
    # Time complexity: O(n)
    # Space complexity: O(1)

    # Two pointer solution
    # Initialize two pointers at the start and end of the array
    # Calculate the area formed by the two lines
    # Move the pointer with the smaller height inwards
    # if the height are the same, move either pointer inwards is fine, and we chose to move the left pointer
    # Keep track of the maximum area and return it

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        area = 0

        while l < r:
            area = max(area, (r - l) * min(height[l], height[r]))

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return area