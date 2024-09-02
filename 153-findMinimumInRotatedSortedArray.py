class Solution(object):
    # Time complexity: O(logn)
    # Space complexity: O(1)

    # Approach: Binary Search
    # 1. If the array is not rotated, then the first element is the minimum element.
    # 2. If the array is rotated, then the minimum element will be the element which is smaller than its previous element.
    # 3. So, we can use binary search to find the minimum element.
    # 4. We can compare the mid element with the left and right elements.
    # 5. If the mid element is greater than the left element, then the minimum element will be in the right half. why? because the left half is sorted.
    # 6. If the mid element is less than the left element, then the minimum element will be in the left half.
    # 7. If the mid element is less than the right element, then the minimum element will be in the right half.
    # 8. If the mid element is greater than the right element, then the minimum element will be in the left half.
    # 9. We can keep updating the minimum element in each iteration.
    # 10. Finally, we will return the minimum element.

    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = [0]
        l,r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            m = (l+r) // 2
            res = min(res, nums[m])

            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        
        return res