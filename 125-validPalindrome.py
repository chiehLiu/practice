class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n) why? because we are creating a new string
    def isPalindrome(self, s: str) -> bool:
        newStr = ""

        for c in s:
            # Alphabetic characters (both uppercase and lowercase letters): A-Z and a-z and Numeric characters: 0-9
            if c.isalnum():
                newStr += c.lower()
        # the :: doing is to reverse the string
        return newStr == newStr[::-1]
    
    # sequence[start:stop:step]
    # •	start and stop omitted: This means the slicing includes the entire sequence.


    # •	start: The starting index (inclusive).
	# •	stop: The stopping index (exclusive).
	# •	step: The step size or increment between each index.

# s = "abcde"
# reversed_s = s[::-1]
# print(reversed_s)  # Output: "edcba"


# Time complexity: O(n)
# Space complexity: O(1)
# why the space complexity is O(1) because we are not creating a new string and we are using the same string
# we are using two pointers to compare the characters
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0, len(s) - 1

        # if l == r stop the loop
        # if l > r stop the loop which means they have crossed each other
        while l < r:
            # since the inner loop here still moving the index, there is possibility that the index will be overlapped, so
            # we need to check if l < r in every l, r pointer movement
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while l < r and not self.alphaNum(s[r]):
                r -= 1
            
            # remember you should compare them in lower case
            if s[l].lower() != s[r].lower():
                return False
            l,r  = l + 1, r - 1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z')) or (ord('a') <= ord(c) <= ord('z')) or (ord('0') <= ord(c) <= ord('9'))
    


# mose recent way to solve the problem
# Time complexity: O(n)
# Space complexity: O(n) because we are creating a new string
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        clean_s = "".join(char for char in s if char.isalnum()).lower()
        
        l, r = 0, len(clean_s) - 1


        while l < r:
            if clean_s[l] != clean_s[r]:
                return False

            if clean_s[l] == clean_s[r]:
                l += 1
                r -= 1
                continue
        
        return True
        


# Time complexity: O(n)
# Space complexity: O(1) because we are not creating a new string
# we are using original string to compare the characters
# This is the most efficient way to solve the problem
class Solution:
    def isPalindrome(self, s):
        l, r = 0, len(s) - 1
        while l < r:

            # the inner while loops are nessessary here to prevent the index from going out of bounds
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
