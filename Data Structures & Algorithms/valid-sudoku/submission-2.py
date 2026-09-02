class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            row = set()
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in row:
                    return False
                row.add(board[i][j])

        for i in range(9):
            column = set()
            for j in range(9):
                if board [j][i] == '.':
                    continue
                if board[j][i] in column:
                    return False
                column.add(board[j][i])
        
        for r in range(0,9,3):
            for c in range(0, 9, 3):
                box = set()
                for i in range(r,r+3):
                    for j in range(c,c+3):
                        if board[i][j] == '.':
                            continue
                        
                        if board[i][j] in box:
                            return False
                        box.add(board[i][j])

        return True        
