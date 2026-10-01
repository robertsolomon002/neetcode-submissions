class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        ROWS = len(grid)
        COLS = len(grid[0])
        globaly_visited = set()

        res = set()


        def makeIsland(row,col,new_set):
            if row >= ROWS or row < 0 or col >= COLS or col < 0 or ((row,col) in globaly_visited):
                return

            if grid[row][col] == 1:

                globaly_visited.add((row,col))
                new_set.add((row,col))

                makeIsland(row+1,col,new_set)
                makeIsland(row,col+1,new_set)

                makeIsland(row-1,col,new_set)
                makeIsland(row,col-1,new_set)


        for i in range(ROWS):
            for j in range(COLS):
                entry = grid[i][j]
                if entry == 1 and ((i,j) not in globaly_visited):
                    island_set = set()
                    makeIsland(i,j,island_set)
                    if len(island_set) > len(res):
                        res = island_set
                    



        return len(res)


        