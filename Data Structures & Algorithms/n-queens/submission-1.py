class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        column = set()
        pos_diag = set() #r + c
        neg_diag = set() #r-c

        res = []

        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r>= n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            row = board[r]
            for col in range(len(row)):
                if (col not in column) and ((col +r) not in pos_diag) and ((r-col) not in neg_diag):
                    column.add(col)
                    pos_diag.add(col+r)
                    neg_diag.add(r-col)

                    row[col] ="Q"
                    backtrack(r+1)

                    row[col] = "."
                    column.remove(col)
                    pos_diag.remove(col+r)
                    neg_diag.remove(r-col)

                



        
        backtrack(0)
        return res
        