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

for i in range(9):
    print(i) # 0 1 2 3 4 5 6 7 8