class Solution(object):
    # Time complexity: O(n)
    # Space complexity: O(min(m, n)), where m is the size of the charset

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        charSet = set()
        res = 0
        l = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r-l+1)
        
        return res