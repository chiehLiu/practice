from collections import defaultdict


# class Solution:
#     def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
#         hash_map = defaultdict(list)

#         for word in strs:
#             # sorted_word = ''.join(sorted(word))
#             sorted_word = tuple(sorted(word))
#             print("sorted_tuple_word:",sorted_word)
#             hash_map[sorted_word].append(word)

#         return list(hash_map.values())

# print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

# for word in strs:
#   print(sorted(word))
  # print(''.join(sorted(word)))

# if you put a number
# it would print from 0 to the number - 1
for i in range(9):
    print(i) # 0 1 2 3 4 5 6 7 8


# it would print the index of the string
# s = "abcde"
for c in range(len(s)):
    print(c) # 0 1 2 3 4


# this is how you iterate all the elements
# s = "abc"
for c in range(s):
    print(c) # a b c