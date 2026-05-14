# Question : According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."
            #The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

              #Any live cell with fewer than two live neighbors dies as if caused by under-population.
              #Any live cell with two or three live neighbors lives on to the next generation.
              #Any live cell with more than three live neighbors dies, as if by over-population.
              #Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
              #The next state of the board is determined by applying the above rules simultaneously to every cell in the current state of the m x n grid board. In this process, births and deaths occur simultaneously.
              #Given the current state of the board, update the board to reflect its next state.
              #Note that you do not need to return anything.

# Time Compleixty : O(m*n)
# Space Complexity : O(1) 

    def gameOfLife(self, board: List[List[int]]) -> None:
        row = len(board)
        col = len(board[0])

        def countNeighbor(r,c):
            nei= 0
            for i in range(r-1,r+2):
                for j in range(c-1,c+2):
                    if ((i==r and j== c) or i <0 or j<0 or i== row or j==col):
                        continue
                    if board[i][j] in [1,3]:
                        nei+= 1
            
            return nei

        for r in range(row):
            for c in range(col):
                neighbor = countNeighbor(r,c)
                if board[r][c]:
                    if neighbor in [2,3]:
                        board[r][c] = 3
                else:
                    if neighbor == 3:
                        board[r][c]= 2
        
        for r in range(row):
            for c in range(col):
                if board[r][c] == 1:
                    board[r][c]= 0
                elif board[r][c] in [2,3]:
                    board[r][c]= 1

 

 

 
