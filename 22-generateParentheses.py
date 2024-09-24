class Solution:
    
    # Time: O(2^n)
    # Space: O(2^n)
    # need to think it through in backtracking section again
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def backtrack(open, close, path):
            if open == close == n:
                res.append(path) 
                return
            
            if open < n:
                backtrack(open + 1, close, path + '(')
            if close < open:
                backtrack(open, close + 1, path + ')')
        
        backtrack(0, 0, '')

        return res