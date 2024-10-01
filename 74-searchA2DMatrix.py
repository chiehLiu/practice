class Solution:
    
    # Time: O(log(m) + log(n))
    # Space: O(1)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        # these are the index of the matrix, and also they are ROWS indices
        top, bot = 0, ROWS - 1

        while top <= bot:
            row = (top + bot) // 2

            # if target is larger than the last ele of the row, then it must be in the next row
            if target > matrix[row][-1]:
                top = row + 1

            # if target is smaller than the first ele of the row, then it must be in the previous row
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        # if the target is not in the matrix
        if not (top <= bot):
            return False
        
        # this is the row containing the target, because we break it here
        row = (top + bot) // 2

        l, r = 0, COLS - 1

        while l <= r:
            m = (l + r) // 2

            # keep in mind that we compare the target with the row we found
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False