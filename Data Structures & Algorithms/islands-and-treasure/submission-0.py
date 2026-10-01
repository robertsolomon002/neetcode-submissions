class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        queue = deque()

        ROWS = len(grid)
        COLS = len(grid[0])

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    queue.append((i,j))
        

        while queue:
            i,j = queue.popleft()

            for x,y in directions:
                ni = i + x
                nj = j + y

                if 0 <= ni < ROWS and 0 <= nj < COLS and grid[ni][nj] >= 214748364:
                    grid[ni][nj] = grid[i][j] + 1
                    queue.append((ni,nj))
            
        


        