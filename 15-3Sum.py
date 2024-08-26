class Solution(object):

    # Time Complexity: O(n^2)
    # Space Complexity: O(n)

    # Approach: Two Pointers
    # 1. Sort the array
    # 2. Iterate over the array and for each element a, find the two sum of the remaining array
    # 3. Use two pointers to find the two sum
    # 4. If the sum is greater than 0, decrement the right pointer
    # 5. If the sum is less than 0, increment the left pointer
    # 6. If the sum is 0, add the triplet to the result
    # 7. Skip the duplicates
    # 8. Return the result

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()

        for i, a in enumerate(nums):

            # Skip the duplicates of the first element
            if i > 0 and a == nums[i-1]:
                continue
            
            l, r = i + 1, len(nums) -1
            while l < r:
                threeSum = a + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1

                # Add the triplet to the result
                # Skip the duplicates

                # The right pointer (r) doesn’t need to be updated in the else block because the two-pointer strategy and the natural flow of the while loop handle any necessary adjustments as the loop progresses.
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
            
        return res