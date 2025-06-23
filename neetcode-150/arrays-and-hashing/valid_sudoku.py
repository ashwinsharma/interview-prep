"""
Submission Link: https://leetcode.com/problems/valid-sudoku/submissions/1673171040
"""

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # validate all rows
        for row in range(9):
            s = set()
            for col in range(9):
                val = board[row][col]
                if val != ".":
                    if val in s:
                        return False
                    else:
                        s.add(val)
        
        # validate all columns
        for col in range(9):
            s = set()
            for row in range(9):
                val = board[row][col]
                if val != ".":
                    if val in s:
                        return False
                    else:
                        s.add(val)
        
        # validate all sub-boxes
        # sub-box 1: rows 0,1,2 | cols 0,1,2
        # sub-box 2: rows 0,1,2 | cols 3,4,5
        # sub-box 3: rows 0,1,2 | cols 6,7,8
        # and so on ...
        boxes = [
            ([0,1,2], [0,1,2]),
            ([0,1,2], [3,4,5]),
            ([0,1,2], [6,7,8]),
            ([3,4,5], [0,1,2]),
            ([3,4,5], [3,4,5]),
            ([3,4,5], [6,7,8]),
            ([6,7,8], [0,1,2]),
            ([6,7,8], [3,4,5]),
            ([6,7,8], [6,7,8])
        ]
        for rows, cols in boxes:
            s = set()
            for row in rows:
                for col in cols:
                    val = board[row][col]
                    if val != ".":
                        if val in s:
                            return False
                        else:
                            s.add(val)
        
        return True
