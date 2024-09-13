class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1) Since we don't use any extra space for the output list as problem description.

    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # demo: [1,2,3,4]
        # [1,1,1,1]
        res = [1] * len(nums)

        for i in range(1, len(nums)):
            # we ignore the 1th ele since it is no prefix
            res[i] = res[i - 1] * nums[i - 1]

        # after the loop the input list would be like:
        # [1, 1, 2, 6]

        # in the iteration we keep track of the postfix product for each element and multiply it with the current res which is the prefix product
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res
