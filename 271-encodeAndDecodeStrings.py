
# Difficulty: Medium
# Time complexity: O(n)
# we only consider while i < len(s) this while loop here, it's O(n) because the length of the string is n
# since the other while loop while s[j] != '#': j += 1 is O(1) because the length of the string is less than 200
# the rest is also O(1)

# Space complexity: O(n)
# Both functions ultimately store all characters from the input strings (in encoded and decoded forms), 
# leading to a total space complexity of O(n) for the entire process. 

# Design an algorithm to encode a list of strings to a string. 
# The encoded string is then sent over the network and is decoded back to the original list of strings.

class Solution:

    # so the strategy is to encode the list of strings into a single string
    # and we add the length of each string and # before it

    # so after encoded, the string will look like this:
    # Input: ["neet","code","love","you"]
    # Output: "4#neet4#code4#love3#you"
  
    def encode(self, strs: list[str]) -> str:
        res = ""
        for s in strs:
            # we use plus equal sign to concatenate the str
            res += str(len(s)) + "#" + s
        return res
            
    # Decodes a single encoded string back into a list of strings.
    # Each string is prefixed with its length and a '#' character.
    def decode(self, s: str) -> list[str]:
        res = []
        i = 0

        # we iterate through the encoded str
        while i < len(s):

            # why j = i? because we want to start from the current index
            # j is the delimiter position
            j = i

            # if the current char is not the delimiter #, we increment j until we find it
            # since 0 <= strs[i].length < 200 the strs length is less than 200, so the steps are constant time like O(3) in worse case, and it's O(1)
            while s[j] != '#':
                j += 1

            # extract the length of the str
            # since we find the delimiter j, we can extract the length
            length = int(s[i:j])

            # j + 1 is the start of the string since the str like this "4#neet4#code"
            i = j + 1

            # i + length is the next start of the string, but we using : to slice the str so we ignore the last index
            j = i + length

            # we got the start and end of the string, so we can extract the string
            res.append(s[i:j])

            # we set i to j, so we can start from the next string
            i = j
        return res
    
    # s = "hello"
    # print(s[1:4])  # Output: 'ell'
    # index 1 is inclusive, index 4 doesn't.