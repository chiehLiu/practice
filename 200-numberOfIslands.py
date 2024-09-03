import collections


class Solution(object):
    
    # DFS
    # Time complexity: O(M x N) where M is the number of rows and N is the number of columns.
    # Space complexity: O(M x N) as the worst case scenario is that all the cells are filled with lands.
    def numIslandsDfs(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        if not grid:
            return 0
        
        def dfs(i, j):
            
            # Check if the cell is out of bounds or is water
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
                return
            
            # Mark the cell as visited
            grid[i][j] = '0'

            # Explore all 4 directions: up, down, left, right
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        nums_islands = 0

        # Iterate through the grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1': # Found a island and start dfs
                    # why dfs ? because we need to explore all the connected islands
                    # and mark them as visited so that we don't count them again
                    dfs(i, j)
                    nums_islands += 1

        return nums_islands        

    # BFS
    # Time complexity: O(M x N) where M is the number of rows and N is the number of columns.
    # Space complexity: O(min(M, N)) because in the worst case where the grid is filled with lands, the size of queue can grow up to min(M, N).
    def numIslandsBFS(self, grid):
      if not grid:
        return 0
    
      def bfs(grid, i, j):
        queue = collections.deque([(i, j)])
        grid[i][j] = '0'  # Mark the cell as visited
        
        while queue:
            x, y = queue.popleft() # pop the first element from the queue
            
            # Explore all adjacent cells (up, down, left, right)
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy # the i and j (which are x and y here) add the dx and dy to explore the adjacent cells
                
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == '1':
                    queue.append((nx, ny)) # if we found the island, add it to the queue and the while loop continues
                    grid[nx][ny] = '0'  # Mark as visited
    
      count = 0
      for i in range(len(grid)):
          for j in range(len(grid[0])):
              if grid[i][j] == '1':
                  count += 1
                  bfs(grid, i, j)
      
      return count