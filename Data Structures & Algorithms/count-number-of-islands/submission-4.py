class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ROW = len(grid)
        COL = len(grid[0])
        explored = set()
        res = 0

        def explore(i,j):
            if not(0<= i < ROW and 0<= j < COL):
                return

            value = grid[i][j]
            
            if value == "0" or (i,j) in explored:
                return
            explored.add((i,j))
            explore(i+1,j)
            explore(i,j+1)
            explore(i-1,j)
            explore(i,j-1)


        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == "1" and ( (row,col) not in explored):
                    explore(row,col)
                    res +=1
        

        return res