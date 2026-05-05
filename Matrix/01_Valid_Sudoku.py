# Question : Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:Each row must contain the digits 1-9 without repetition.Each column must contain the digits 1-9 without repetition.Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:A Sudoku board (partially filled) could be valid but is not necessarily solvable.Only the filled cells need to be validated according to the mentioned rules.

# Time Complexity : O(1)

# Space Complexity : O(1) 



def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            s = set()
            for j in range(9):
                if board[i][j] in s:
                    return False
                elif board[i][j]!= '.':
                    s.add(board[i][j])
        for i in range(9):
            s = set()
            for j in range(9):
                if board[j][i] in s:
                    return False
                elif board[j][i]!= '.':
                    s.add(board[j][i])
        
        start = [(0,0),(0,3),(0,6)
                ,(3,0),(3,3),(3,6)
                ,(6,0),(6,3),(6,6)]

        for row, col in start:
            s= set()
            for i in range(row,row+3):
                for j in range(col,col+3):
                    if board[i][j] in s:
                        return False
                    elif board[i][j]!= '.':
                        s.add(board[i][j])

        return True
