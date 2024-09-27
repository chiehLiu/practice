class Solution:
    # Time: O(logn) log base 2 of n equals to the number of times we can divide n by 2 until we get 1
    # Space: O(1)

    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
          m = (r + l) // 2 # this is the same as (r - l) // 2 + l
          if nums[m] > target:
            r = m - 1
          elif nums[m] < target:
            l = m + 1
          else:
            return m
        
        return -1