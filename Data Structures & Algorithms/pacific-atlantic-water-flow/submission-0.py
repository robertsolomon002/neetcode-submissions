class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pq = deque()
        aq = deque()
        
        pset = set()
        aset = set()

        ROWS = len(heights)
        COLS = len(heights[0])

        for j in range(COLS):
            if j == 0:
                pq.append((0,j))
                pq.append((ROWS-1,j))
                aq.append((ROWS-1,j))
            elif j == COLS -1:
                pq.append((0,j))
                aq.append((0,j))
                aq.append((ROWS-1,j))
            else:
                pq.append((0,j))
                aq.append((ROWS-1,j))
        for i in range(ROWS):
            if i != 0 and i != ROWS-1:
                pq.append((i,0))
                aq.append((i,COLS-1))


        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while pq:
            i,j = pq.popleft()
            pset.add((i,j))

            for x,y in directions:
                ni,nj = i+x, j+y

                if 0<= ni < ROWS and 0 <= nj < COLS and ((ni,nj) not in pset) and heights[i][j] <= heights[ni][nj]:
                    pq.append((ni,nj))



        while aq:
            i,j = aq.popleft()
            aset.add((i,j))

            for x,y in directions:
                ni,nj = i+x, j+y

                if 0<= ni < ROWS and 0 <= nj < COLS and ((ni,nj) not in aset) and heights[i][j] <= heights[ni][nj]:
                    aq.append((ni,nj))

        result = []
        for i,j in aset.intersection(pset):
            result.append([i,j])

        
        return result
        