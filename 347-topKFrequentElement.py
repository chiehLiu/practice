class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
      count = {}
      # create a list of list with the length of nums + 1
      # why + 1? because the index starts at 0
      freq = [[] for i in range(len(nums) + 1)]

      for n in nums:
        count[n] = 1 + count.get(n, 0)
      for n, c in count.items():
        # set the c->count as index and n->number as value
        freq[c].append(n)
        print("freq:",freq)

      res = []

      # iterate from the end of the list->len(freq) - 1
      # to the beginning of the list->0
      # and decrement by 1
      # the reason why we iterate from the end is because the biggest count at the end of the list.
      # so we append the kth element to res and when it reaches k, we return res
      for i in range(len(freq) - 1, 0, -1):

        # iterate through the count because it will multiple numbers with the same count
        for n in freq[i]:
          res.append(n)
          if len(res) == k:
            return res

# print a list with multiple numbers with same count
# give me a demo here: [1, 1, 1, 2, 2, 3]

# print(Solution().topKFrequent([1,1,1,2,2,2,3], 2))  => [1,2]