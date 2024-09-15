import collections


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
      cols = collections.defaultdict(set) 
      rows = collections.defaultdict(set)
      squares = collections.defaultdict(set) # key: (r/3, c/3)

      for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
              continue
            if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3, c//3)]:
              return False
            rows[r].add(board[r][c])
            cols[c].add(board[r][c])
            squares[(r//3, c//3)].add(board[r][c]) # (r//3, c//3) is the key for the square, and we use tuple here because we can't use list as a key in a dictionary
      
      return True
    

# demo:

# 5 3 . | . 7 . | . . .
# 6 . . | 1 9 5 | . . .
# . 9 8 | . . . | . 6 .
# ------+-------+------
# 8 . . | . 6 . | . . 3
# 4 . . | 8 . 3 | . . 1
# 7 . . | . 2 . | . . 6
# ------+-------+------
# . 6 . | . . . | 2 8 .
# . . . | 4 1 9 | . . 5
# . . . | . 8 . | . 7 9

# the squares dict will look like this:
# 0, 1, 2 // 3 = 0
# 3, 4, 5 // 3 = 1
# 6, 7, 8 // 3 = 2

# "//" operator means floor division, which means the result is the whole number, not the decimal
# it will rounds down the result to the nearest whole number.
# what is round down means? ex. 0.6 => 0, 1.2 => 1, 1.9 => 1, 2.5 => 2, 3.1 => 3

# {
#   (0, 0): {'5', '3', '6', '9', '8'},   # Top-left 3x3 square
#   (0, 1): {'7', '1', '9', '5'},         # Top-middle 3x3 square
#   (0, 2): {'6'},                        # Top-right 3x3 square
#   (1, 0): {'8', '4', '7'},              # Middle-left 3x3 square
#   (1, 1): {'6', '8', '3', '2'},         # Middle-middle 3x3 square
#   (1, 2): {'3', '1', '6'},              # Middle-right 3x3 square
#   (2, 0): {'6'},                        # Bottom-left 3x3 square
#   (2, 1): {'4', '1', '9', '8'},         # Bottom-middle 3x3 square
#   (2, 2): {'2', '8', '5', '7', '9'}     # Bottom-right 3x3 square
# }

# the rows dict will look like this:
# {
#   0: {'5', '3', '7'},         # First row: numbers 5, 3, and 7
#   1: {'6', '1', '9', '5'},    # Second row: numbers 6, 1, 9, 5
#   2: {'9', '8', '6'},         # Third row: numbers 9, 8, 6
#   3: {'8', '6', '3'},         # Fourth row: numbers 8, 6, 3
#   4: {'4', '8', '3', '1'},    # Fifth row: numbers 4, 8, 3, 1
#   5: {'7', '2', '6'},         # Sixth row: numbers 7, 2, 6
#   6: {'6', '2', '8'},         # Seventh row: numbers 6, 2, 8
#   7: {'4', '1', '9', '5'},    # Eighth row: numbers 4, 1, 9, 5
#   8: {'8', '7', '9'}          # Ninth row: numbers 8, 7, 9
# }

# the cols dict will look like this:
# {
#   0: {'5', '6', '8', '4', '7'},    # First column: numbers 5, 6, 8, 4, 7
#   1: {'3', '9', '4', '6', '1'},    # Second column: numbers 3, 9, 4, 6, 1
#   2: {'7', '8', '6', '7', '9'},    # Third column: numbers 7, 8, 6, 7, 9
#   3: {'1', '8', '4'},              # Fourth column: numbers 1, 8, 4
#   4: {'9', '6', '8', '1'},         # Fifth column: numbers 9, 6, 8, 1
#   5: {'5', '3', '1', '9'},         # Sixth column: numbers 5, 3, 1, 9
#   6: {'6', '2'},                   # Seventh column: numbers 6, 2
#   7: {'8', '8', '2'},              # Eighth column: numbers 8, 8, 2
#   8: {'3', '1', '6', '5'}          # Ninth column: numbers 3, 1, 6, 5
# }