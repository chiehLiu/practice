class Solution(object):
    # Time complexity: O(n)
    # Space complexity: O(min(m, n)), where m is the size of the charset

    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        sub = set()

        for r in range(len(s)):
            
            # meet the duplicate we pop the left most ele
            # because this substring can't extend anymore
            while s[r] in sub:
                sub.remove(s[l])
                l += 1

            sub.add(s[r])
            res = max(res, r - l + 1)
        
        return res