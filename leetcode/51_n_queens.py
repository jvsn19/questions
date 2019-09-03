class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.boards = []
        to_return = []
        
        def valid_board(board, curr_col):
            for prev_col in range(0, curr_col):
                prev_row = board[prev_col]
                curr_row = board[curr_col]
                
                if prev_row == curr_row or abs(prev_row - curr_row) == abs(prev_col - curr_col):
                    return False

            return True
        
        def helper(col, board):
            if col == n:
                self.boards.append(board)
                return
            
            for row in range(n):                
                if not valid_board(board + [row], col):
                    continue
                helper(col + 1, board + [row])
                
        helper(0, [])
        
        for board in self.boards:
            matrix = []
            
            for col_pos in board:
                row = ['Q' if pos == col_pos else '.' for pos in range(n)]
                matrix.append(''.join(row))
            
            to_return.append(matrix)        
        return to_return