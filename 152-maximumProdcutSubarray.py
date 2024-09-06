class Solution:
    
    # Time: O(n)
    # Space: O(1)

    # Approach: Kadane's Algorithm
    # 1. Initialize res as max(nums)
    # 2. Initialize curMin and curMax as 1
    # 3. Iterate through the list
    # 4. If n == 0, reset curMin and curMax to 1
    # 5. Memorize curMax in tmp
    # 6. Compare n, curMax * n, curMin * n
    # 7. Update curMax and curMin
    # 8. Update res

    def maxProduct(self, nums: List[int]) -> int:
        # why res initialized as max(nums) instead of 0?
        # because if there is only one element in the list, the result should be that element
        res = max(nums)

        # curMin and curMax initialized as 1 because it s neutral element for multiplication
        curMin, curMax = 1, 1

        for n in nums:
            # if n == 0, reset curMin and curMax to 1
            # since we already store the result in res, we don't need to update res
            if n == 0:
                curMin, curMax = 1, 1
                continue
            
            # why we memorize curMax in tmp?
            # because curMax will be updated in the next line, so we need to memorize it
            # and use it to update curMin
            tmp = curMax

            # why we compare n, curMax * n, curMin * n?
            # because we need to consider the case when n is negative

            # if n is negative, curMax * n will be the new curMin
            # if n is negative, curMin * n will be the new curMax

            # why we need to include n in the comparison?
            # because n itself can be the new curMax or curMin

            curMax = max(n, curMax * n, curMin * n)
            curMin = min(n, tmp * n, curMin * n)
            res = max(res, curMax)
        return res