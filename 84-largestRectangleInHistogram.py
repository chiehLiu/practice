class Solution:
    
    # Time: O(n)
    # Space: O(n)

    # this one is hard, need more grinding
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # pair: [index, height]

        for i, h in enumerate(heights):
            start = i 
            
            # do the pop and calculate the area
            # when the current height is smaller than the last height in the stack
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                # we only calculate the area when the height been popped
                maxArea = max(maxArea, height * (i - index))

                # since we pop the last height, we still need to extend the width because the current height is smaller than the last height, so we can extend the width to the last height
                # so we update it's index to start
                start = index
            # we append the start because we need to extend the width of the rectangle to those popped heights
            stack.append((start, h))

        # the remaining stack is in increasing order(heights)
        # so we using the len(heights) - i it presents the width of the rectangle
        # since the smaller height will extend the width to the end

        # Example with heights = [2, 1, 5, 6, 2, 3]:
        # At the end, the stack is [(0, 1), (2, 2), (5, 3)]:
        # The index here were extended forward like the (2,2) the original would be (4,2) and the rest of the stack are all extendable, so we just use the length of the heights to minus the index to get the width

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        
        return maxArea