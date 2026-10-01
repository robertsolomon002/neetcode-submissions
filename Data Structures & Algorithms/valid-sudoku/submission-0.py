class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = {}
        col_map = {}
        square_map ={}

        for k in range(9):
            row_map[k] = set()
            col_map[k] = set()
            square_map[k] = set()
        
        for i in range(9):
            for j in range(9):
                entry = board[i][j]
                if entry.isdigit():
                    entry = int(entry)
                    row_ind = i
                    col_ind = j
                    box_ind = (i // 3) *3 + (j // 3)
                    print(box_ind)
                    if entry in row_map[row_ind] or entry in col_map[j] or entry in square_map[box_ind]:
                        return False
                    else:
                        row_map[row_ind].add(entry)
                        col_map[j].add(entry)
                        square_map[box_ind].add(entry)
        

        return True

        