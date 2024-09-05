class Solution:
    # Time: O(m*n)
    # Space: O(m*n)

    # Approach: DFS

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        # collecting the water reachable to pacific and atlantic
        pac_reachable, atl_reachable = set(), set()

        def dfs(r, c, visited, preHeight):
            # if r, c in visited means already visited just return
            # if r, c is out of bound or height is less than previous height then return
            # why we checkout heights[r][c] < preHeight ? because we check in reverse order, from outer to inner
            if (r, c) in visited or r < 0 or c < 0 or r == ROWS or c == COLS or heights[r][c] < preHeight:
                return
            
            # add the current cell to visited, meaning we found a reachable cell
            visited.add((r, c))

            # check for all directions
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                dfs(r+dr, c+dc, visited, heights[r][c])
            
        # start from the pacific and atlantic borders
        for c in range(COLS):
            # pacific
            dfs(0, c, pac_reachable, heights[0][c])

            # atlantic
            dfs(ROWS-1, c, atl_reachable, heights[ROWS-1][c])

        # start from the pacific and atlantic borders
        for r in range(ROWS):
            
            # pacific
            dfs(r, 0, pac_reachable, heights[r][0])
            # atlantic
            dfs(r, COLS-1, atl_reachable, heights[r][COLS-1])

        # return list(pac_reachable.intersection(atl_reachable))

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac_reachable and (r, c) in atl_reachable:
                    res.append([r, c])
        
        return res