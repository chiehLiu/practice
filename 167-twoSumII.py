class Solution:
    # Time: O(n)
    # Space: O(1)

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # although the problem is 1-indices, we still have to use 0-indices because of the while loop

        # in short we are set the l,r pointers in list, so we still need the start to be 0 and the end to be len(numbers) -1
        # in that case the "indexError" will not happen
        l,r = 0, len(numbers)-1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l+1, r+1]
            