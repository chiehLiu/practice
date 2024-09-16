class Solution:
    # Time: O(n)
    # Space: O(n)
    def longestConsecutive(self, nums: List[int]) -> int:
        # use Set to store the numbers and get rid of duplicates
        newSet = set(nums)
        longest = 0

        for i in newSet:
            if (i - 1) not in newSet:
                
                # the length here is the increment value of the current number
                # since the consecutive sequence is increasing by 1, we can use length to check the next number and update the longest
                length = 0

                # use i + length to check if the next number is in the set
                while(i + length) in newSet:
                    # if the next number is in the set, increase the length
                    length += 1
                longest = max(length, longest)
        return longest
