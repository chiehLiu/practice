class Solution:
    # Time: O(n^2)
    # Space: O(1)

    # Approach: Expand around center
    # For each character in the string, we will expand around it to check if it is a palindrome
    # we will have two cases:
    # 1. Expand around a single character
    # 2. Expand around two characters
    # We will keep track of the count of palindromes we find
    # We will return the count at the end

    def countSubstrings(self, s: str) -> int:
        res = 0
        
        # For each character in the string
        for i in range(len(s)):
            
            # Case 1: Expand around a single character
            # l, and r are the same and we expand around it
            res += self.countPali(s, i, i)

            # Case 2: Expand around two characters
            # l and r are one apart and we expand around it
            res += self.countPali(s, i, i + 1)
        return res

    def countPali(self, s, l, r):
        res = 0

        # make sure l is greater than or equal to the first character
        # and r is less than the length of the string
        # and the characters at l and r are the same if they are, we increment the res and expand the window
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res