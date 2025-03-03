# this question need to deal with index so be careful about the boundaries on base cases or loops.

# cur.pop() is necessary to:
# 	•	Undo the last inclusion before moving to the next possibility.
# 	•	Ensure correct subsets are formed without persisting unwanted elements across recursive calls.
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if total > target or i == len(candidates):
                return
            
            #Include the current ele
            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])
            cur.pop()

            #Skip the current ele
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
              i += 1
            dfs(i + 1, cur, total)
        
        dfs(0, [], 0)
        return res