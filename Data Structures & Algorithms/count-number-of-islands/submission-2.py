class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ROWS = len(grid)
        COLS = len(grid[0])

        res = []

        globally_visited = set()

        def makeIsland(row,col):
            if row >= ROWS or col >=COLS or ((row,col) in globally_visited) or row < 0 or col <0:
                return
            globally_visited.add((row,col))

            value = grid[row][col]
            #print(i,j)

            if value == "1":
                makeIsland(row +1,col)
                makeIsland(row, col +1)
                makeIsland(row -1,col)
                makeIsland(row, col -1)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                entry = grid[i][j]
                #print((i,j))
                #print(grid[i][j] == "1" )
                #print((i,j) not in globally_visited)
                if (grid[i][j] == "1" )and ((i,j) not in globally_visited):
                    #print(globally_visited)
                    #print((i,j))
                    island_set = set()
                    island_set.add((i,j))
                    makeIsland(i,j)
                    res.append(island_set)

                #globally_visited.add((i,j))

        print(res)
        return len(res)
        