class Solution:
    # Time: O(logn)
    # Space: O(1)
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]

        while l <= r:

            # meaning it's been sorted
            # it's important to come up with this condition
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) //2

            # update the res every time we recalculate the m
            res = min(res, nums[m])

            # search right
            if nums[m] >= nums[l]:
                l = m + 1
            # search left
            else:
                r = m - 1
        
        return res
