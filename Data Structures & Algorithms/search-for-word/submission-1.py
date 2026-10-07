class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        y_len = len(board)
        x_len = len(board[0])
        path = set()



        def dfs(x,y,i):
            if i >= len(word):
                return True
                            
            if not (0 <= x < x_len) or (0 <= y <y_len) or (board[y][x] != word[i]) or ((x,y) in path):
                return False

            path.add((x,y))
            res = dfs(x+1,y,i+1) or dfs(x-1,y,i+1) or dfs(x,y +1,i+1) or dfs(x,y -1,i+1)
            path.remove((x,y))
            return res


            
        for r in range(y_len):
            for c in range(x_len):
                if dfs(c,r,0):
                    return True
        return False
        