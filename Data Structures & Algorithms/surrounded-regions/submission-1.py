class Solution:
    def solve(self, board: List[List[str]]) -> None:

        q = deque()

        ROWS = len(board)
        COLS = len(board[0])

        set_O = set()

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O":
                    

                    if i == 0 or i == ROWS -1 or j == 0 or j ==  COLS -1:
                        q.append((i,j))
                    else:
                        set_O.add((i,j))


        direction = [(0,1),(1,0),(0,-1),(-1,0)]
        while q:
            i,j = q.popleft()
            if (i,j) in set_O:
                set_O.remove((i,j))

            for x,y in direction:
                ni,nj = i+x, j+y

                if 0<= ni < ROWS and 0<= nj <COLS and ((ni,nj) in set_O):
                    q.append((ni,nj))
        
        for i,j in set_O:
            board[i][j] = "X"
        print(set_O)




        print(q)
        