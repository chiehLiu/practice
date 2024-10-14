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
    
    class Solution:
        def characterReplacement(self, s: str, k: int) -> int:
            # Create a defaultdict with a default value of an empty integer
            sub = defaultdict(int)
            l, r = 0, 0
            res = 0

            while r <= len(s) - 1:
                # 1. we need to build the sub dictionary to count every elements in s
                # 2. we use the windowLen subtract the most frequent ele and check is it smaller and equal to k,
                # in that case the window would be valid
                # if the window is invalid we increment the l pointer
                # if in does valid we update the res and move on to the next r till the end of the s string

                windowLen = r - l + 1

                sub[s[r]] += 1
                
                # the most important point in this question is to find the valid window
                if windowLen - max(sub.values()) <= k:
                    res = max(res, windowLen)
                else:
                    sub[s[l]] -= 1
                    l += 1
                
                r += 1
            
            return res
        
        # if the s = ABAACSASVF, k =2
        # what would be the sub looks like?
        # sub = {A: 3, B: 1, C: 1, S: 2, V: 1, F: 1}