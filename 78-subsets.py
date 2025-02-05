
# time: O(n * 2^n)
# space: O(n)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i == len(nums):
                # don't mutate the subset, so we need to copy it
                res.append(subset.copy())
                return
            
            # include the current element
            subset.append(nums[i])
            dfs(i + 1)

            # exclude the current element
            res.pop()
            dfs(i + 1)
        dfs(0)
        return res