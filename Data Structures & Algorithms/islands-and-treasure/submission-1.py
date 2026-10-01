class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        q = deque()

        ROWS = len(grid)
        COLS = len(grid[0])

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append((i,j))

        
        moves = [(0,-1),(0,1),(1,0),(-1,0)]

        while q:
            i,j = q.popleft()
            for x,y in moves:
                ni = i +x
                nj = j +y

                if 0 <= ni < ROWS and 0 <= nj < COLS and grid[ni][nj] >= 1000:
                    grid[ni][nj] = grid[i][j] +1
                    q.append((ni,nj))



            
        


        