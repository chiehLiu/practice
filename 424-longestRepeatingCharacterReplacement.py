class Solution(object):
    # Time complexity: O(n)
    # Space complexity: O(1)

    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = {}
        res = 0
        l = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0) # the second argument is the default value
            
            # if the length of the window minus the max count of the character in the window is greater than k
            while (r - l + 1) - max(count.values()) > k:
                # subtract the count of the character at the left end of the window and move the window to the right
                count[s[l]] -= 1
                l += 1

            res = max(res, r - 1 + 1)
        return res