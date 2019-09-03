class Solution:
    def totalNQueens(self, n: int) -> List[List[str]]:
        self.answer = 0
        
        def valid_board(board, curr_col):
            for prev_col in range(0, curr_col):
                prev_row = board[prev_col]
                curr_row = board[curr_col]
                
                if prev_row == curr_row or abs(prev_row - curr_row) == abs(prev_col - curr_col):
                    return False

            return True
        
        def helper(col, board):
            if col == n:
                self.answer += 1
            
            for row in range(n):                
                if not valid_board(board + [row], col):
                    continue
                helper(col + 1, board + [row])
                
        helper(0, [])
        
        return self.answer