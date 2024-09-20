class Solution(object):
    # Time Complexity: O(n^2)
    # Space Complexity: O(n) since we are using the res array to store the results

    # Approach: Two Pointers
    # 1. Sort the array
    # 2. iterate through the array and we use enumerate to get the index and the value
    # 3. check if current index is greater than 0 also current value is no the same as the previous value, if not continue
    # 4. set the pointers
    # 5. while left is less than right loop through the array
    # 6. if threeSum is greater than 0, decrement the right pointer
    # 7. if threeSum is less than 0, increment the left pointer
    # 8. if threeSum is 0, append the result
    # 9. increment the left pointer and skip the duplicates

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()

        for i, a in enumerate(nums):

            # Skip the duplicates, and it only happens after second iteration
            # since there is no duplicates in the first iteration
            if i > 0 and a == nums[i-1]:
                continue
            
            l, r = i + 1, len(nums) -1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                
                # the reason why we don't check duplicates here is because we only check it when we found the valid threeSum, and we make sure we don't duplicate the result
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    # we can move l or r, it doesn't matter
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    # as we increment the l index, we need to check if the next element is the same
                    # if it is, we need to skip it
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
            
        return res