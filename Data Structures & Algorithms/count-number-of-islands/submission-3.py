class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()

        direction =[(0,+1),(+1,0),(-1,0),(0,-1)]
        def find_island(i,j):
            visited.add((i,j))

            for d1,d2 in direction:
                x1,y1 = i+d1,j+d2
                if 0 <= x1 < len(grid) and 0 <= y1 < len(grid[0]) and ((x1,y1) not in visited) and grid[x1][y1] =="1":
                    find_island(x1,y1)
        res = 0

        for l in range(len(grid)):
            for k in range(len(grid[0])):
                if ((l,k) not in visited):
                    print(l,k)
                    if grid[l][k] == "1":
                        find_island(l,k)
                        res +=1
                        #print(l,k)
                    else:
                        visited.add((l,k))
        
        return res

        