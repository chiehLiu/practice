class Solution:
    # Time: O(n) where n is the length of s2
    # Space: O(1) since we are using fixed size arrays

    # still not sure why this works
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = [0] * 26
        s2Count = [0] * 26

        for c in s1:
            s1Count[ord(c) - ord("a")] += 1

        # Sliding window
        for i in range(len(s2)):
            # Add the current character to the window
            s2Count[ord(s2[i]) - ord("a")] += 1

            # if the window is larger than s1, remove the first character from the window
            if i >= len(s1):
                
                # Remove the first character from the window
                indexOfCharToRemove = i - len(s1)
                s2Count[ord(s2[indexOfCharToRemove]) - ord("a")] -= 1

            if s1Count == s2Count:
                return True
        return False