class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        maxI = 0
        countI = 1

        for i in range(len(nums)):
            if i + 1 > len(nums) - 1:
                break

            if nums[i + 1] > nums[i]:
                countI += 1
                maxI = max(maxI, countI)
            else:
                countI = 1
                maxI = max(maxI, countI)

        maxD = 0
        countD = 1

        for i in range(len(nums)):
            if i + 1 > len(nums) - 1:
                break

            if nums[i + 1] < nums[i]:
                countD += 1
                maxD = max(maxD, countD)
            else:
                countD = 1
                maxD = max(maxD, countD)
        
        res = max(maxD, maxI)
        
        return res

            


            