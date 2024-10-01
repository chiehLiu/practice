class Solution:
    # Time: O(logn)
    # Space: O(1)

    # no idea what the fuck is this, will do it tomorrow again.
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            # meaning the nums[m] is in the left part and so far the biggest one, but there is chance that still bigger one after m

            # the outer if check tells us which part the nums[m] is in

            # in left part
            if nums[l] <= nums[m]:

                # if target bigger than nums[m] we move to the right
                # or target smaller than nums[m] and smaller than nums[l] meaning target is not in the left part so we move to the right
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                
                # if target smaller than nums[m] meaning it is in the left part we move to the left
                # or target bigger than nums[m] and bigger than nums[r] meaning target is not in the right part so we move to the left
                else:
                    r = m - 1

            # meaning the nums[m] is in the right part and so far the smallest one, but there is chance that still smaller one before m

            # in right part
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1