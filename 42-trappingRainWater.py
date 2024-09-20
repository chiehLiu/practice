class Solution:
    # Time: O(n^2)
    # Space: O(1)

    # Brute Force
    # first check the height is not empty
    # loop through the height
    # find the max l, r height
    # the min of max l, r height minus the current height and add to the water
    # return the water

    def trap(self, height: List[int]) -> int:

      if not height:
        return 0

      for i in range(height):
        maxL = max(height[:i+1])
        maxR = max(height[i:])

        water += min(maxL, maxR) - height[i]
      return water

class Solution:
    
    # Time: O(n)
    # Space: O(1)

    # Two Pointers
    # first check the height is not empty
    # set the l, r to 0, and the last index of the height
    # set the maxL, maxR to the first and last of the height
    # while l is less than r
    # check if maxL is less than maxR
    # if it is, increment l by 1
    # update the maxL to the max of maxL and height[l]
    # if not, decrement r by 1
    # update the maxR to use the max of maxR and height[r]
    # add the max of maxL, maxR minus the current height to the water
    # return the water
    def trap(self, height: List[int]) -> int:

      if not height:
        return 0
      
      water = 0
      l, r = 0, len(height) - 1
      maxL = height[l]
      maxR = height[r]

      while l < r:
        if maxL < maxR:
          l += 1
          maxL = max(maxL, height[l])

          # we don't need to worry about negative value because we are update the maxL in the last line,
          # so the maxL will always be greater or equal to height[l], if in the r case it's the same.
          water += maxL - height[l]
        else:
          r -= 1
          maxR = max(maxR, height[r])
          water += maxR - height[r]
      
      return water