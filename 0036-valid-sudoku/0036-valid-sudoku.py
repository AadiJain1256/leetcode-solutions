class Solution(object):
    def isValidSudoku(self, board):
        
        row={}
        column={}
        box={}
        for a in range(9):
            row[a]=set()
            column[a]=set()

        for i in range(3):
            for j in range(3):
                box[(i,j)]=set()

        for r in range(9):
            for c in range(9):
                if board[r][c]==".":
                    continue
                b=(r//3,c//3) 
                if ((board[r][c] in row[r])or
                    (board[r][c] in column[c])or
                    (board[r][c] in box[b])):
                    return False

                row[r].add(board[r][c])
                column[c].add(board[r][c])
                box[b].add(board[r][c])

        return True