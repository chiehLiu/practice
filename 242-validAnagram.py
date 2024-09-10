class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        # O(n) time complexity
        # O(1) space complexity because the size of the dictionary is fixed like 26 characters

        if len(s) != len(t):
            return False
        
        # Counter(s) creates a Counter object, which is essentially a specialized dictionary 
        # where the keys are elements from the string s (in this case, characters), 
        # and the values are the counts of those elements.
        s_count = collections.Counter(s)
        t_count = collections.Counter(t)

        # s_count.items() returns a dict_items view object, which behaves like a set of tuples.
        # dict_items([('a', 3), ('n', 1), ('g', 1), ('r', 1), ('m', 1)])
        # you can loop over this dic_items object in a for loop, 
        # which is common when you want to process key-value pairs from a dictionary or a Counter object.
        for key, value in s_count.items():
            if key in t_count:
                if value != t_count[key]:
                    return False
            else:
                return False

        return True
      

# # collections.Counter() function demo

# from collections import Counter
# # Example string
# s = "anagram"

# # Create a Counter object
# s_count = Counter(s)

# # Output the Counter object
# print(s_count)

# and the output will be:
# Counter({'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1})


# using hash map
# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = {}

        if len(s) != len(t):
            return False

        for c in s:
            if c in hash_map:
                hash_map[c] += 1
            else:
                hash_map[c] = 1
        
        for ch in t:
            if ch in hash_map:
                hash_map[ch] -= 1

                if hash_map[ch] == 0:
                    del hash_map[ch]
            
        return True if len(hash_map) == 0 else False
    

    # using hash map
    # cleaner version
    class Solution:
        def isAnagram(self, s: str, t: str) -> bool:
            if len(s) != len(t):
                return False

            countS, countT = {}, {}

            for i in range(len(s)):
                countS[s[i]] = 1 + countS.get(s[i], 0)
                countT[t[i]] = 1 + countT.get(t[i], 0)
            return countS == countT