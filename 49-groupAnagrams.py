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

        # by passing list as the argument to the defaultdict function, you can specify that the default value for any key that doesn't exit in the dictionary is an empty list[]
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

# this method is more reasonable to think about the problem
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))

            if sorted_word in hash_map:
                hash_map[sorted_word].append(word)
            else:
                hash_map[sorted_word] = [word]

        # the reason we use list to convert the values of the hash_map is because the values of the hash_map are div_values it's an view object
        # so we need to convert it to a list
        return list(hash_map.values())
    
# word = "cat"
# the sorted func would return a list of characters like this: ['a', 'c', 't']
# the join func would return a string like this: 'act'
# sorted_word = ''.join(sorted(word))
# print(sorted_word)



# this method is more efficient than the previous one
# because we are using a tuple as the key of the hash_map
# and we use the count of the characters in the word as the key
# so we don't need to sort the word

# the time complexity of this method is O(n * k)
# the space complexity of this method is O(n * k)

# n -> number of strings in the input list
# k -> maximum length of a string in the input list, which is 26 so it's a constant
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()