class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        # Initialize the answer window and the count of characters in t
        window, countT = {}, {}

        # Count the characters in t and fill in the countT dictionary
        for c in t:
            countT[c] = countT.get(c, 0) + 1
        
        # have is the number of characters in the window that can be used to form t
        # need is the number of characters needed to form t
        have, need = 0, len(countT)
        # set res = [-1, -1] because no valid window has been found yet, so this value indicates an invalid or uninitialized state.
        # because you want to find the minimum window length, so you start with the largest possible value.
        res, resLen = [-1, -1], float('inf')
        l = 0
        for r in range(len(s)):
            # extract c from the s string
            c = s[r]
            # update the window key is c and value is the count of c in the window
            window[c] = window.get(c, 0) + 1

            if c in countT and window[c] == countT[c]:
                have += 1
            
            # if the window has all the characters needed to form t
            while have == need:
                
                # update the result
                # the condition here use less than because we want to find the minimum window
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                # pop from the left of the window

                # subtract the count of the character at the left of the window
                window[s[l]] -= 1

                # if the character l in countT
                # and the count of the character l in the window is less than the count of the character l in countT
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        
        # what this line does it
        # If res = [x, y], this line will assign:
        # l = x
        # r = y
        l, r = res

        # s[l:r+1] meaning start from index l and go up to (and including) index r. The +1 is used to include the character at index r in the slice.
        # if resLen is still float('inf') then return an empty string, meaning no valid window was found.
        return s[l:r+1] if resLen != float('inf') else ""
