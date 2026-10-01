class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(1,0),(-1,0),(0,-1),(0,1)]

        q = deque()
        time = 0
        fresh = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    fresh +=1

        while q and fresh > 0:
            for _ in range(len(q)):
                i,j = q.popleft()
                for d in directions:
                    ni,nj = i+d[0], j + d[1]

                    if 0 <= ni < ROWS and 0 <= nj < COLS and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        fresh -= 1
                        q.append((ni,nj))
            time +=1
        
        if fresh > 0:
            return -1
        
        else:
            return time