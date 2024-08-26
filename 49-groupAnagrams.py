from collections import defaultdict

class Solution(object):

    # Time complexity: O(n * k log k)
    # Space complexity: O(n * k)

    # n -> number of strings in the input list
    # k -> maximum length of a string in the input list

    # The time complexity is O(n * k log k) because we are iterating through the list of strings and sorting each string
    # The space complexity is O(n * k) because we are storing the sorted strings in a dictionary

    # This approach is based on the idea that two strings are anagrams if they have the same sorted string
    # We can use this property to group anagrams together
    # We create a dictionary to store the sorted strings as keys and the original strings as values
    # We then return the values of the dictionary as a list of lists

    # 1. Create a dictionary to store the anagrams
    # 2. Iterate through the list of strings
    # 3. Sort each string and use it as a key in the dictionary
    # 4. Append the original string to the list of anagrams for that key
    # 5. Return the values of the dictionary as a list of lists

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        # the defaultdict looks like this:
        # {('a', 'e', 't'): ['eat', 'tea', 'ate']}

        # the anagrams looks like this:
        # {'aet': ['eat', 'tea', 'ate']}

        anagrams = defaultdict(list)
    
        for s in strs:
            # Sort the string and use it as a key
            # and the key looks like this: ('a', 'e', 't')

            # Python dictionaries require keys to be immutable (i.e., they cannot change). 
            # While a list can hold the sorted # characters, lists are mutable, so they can't be used directly as dictionary keys.
            # A tuple, on the other hand, is immutable, making it a suitable key for a dictionary.
            key = tuple(sorted(s))
            anagrams[key].append(s)
        
        return list(anagrams.values())
    
#     {
#     ('a', 'e', 't'): ['eat', 'tea', 'ate'],
#     ('a', 'n', 't'): ['tan', 'nat'],
#     ('a', 'b', 't'): ['bat']
#     }
