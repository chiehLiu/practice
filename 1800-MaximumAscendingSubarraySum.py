class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        maxSum = max(nums)
        curSum = nums[0]
        
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                curSum += nums[i + 1]
            else:
                maxSum = max(curSum, maxSum)
                curSum = nums[i + 1]

        
        return max(maxSum, curSum)

