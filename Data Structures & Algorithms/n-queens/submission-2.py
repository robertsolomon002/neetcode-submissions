class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        column = set()
        pos_diag = set() #i + j
        neg_diag = set() # i - j


        result = []
        board = [["."] * n for i in range(n)]

        def backtrack(i):
            if i >= n:
                copy = ["".join(row) for row in board]
                result.append(copy)
                return

            actual_row = board[i]

            for j in range(n):
                if (j not in column) and (j +i not in pos_diag) and (i-j not in neg_diag):
                    column.add(j)
                    pos_diag.add(j+i)
                    neg_diag.add(i-j)
                    actual_row[j] = "Q"
                    backtrack(i+1)
                    column.remove(j)
                    pos_diag.remove(j+i)
                    neg_diag.remove(i-j)
                    actual_row[j] = "."

        
        backtrack(0)

        return result