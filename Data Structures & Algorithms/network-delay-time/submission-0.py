class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        vertMap = {i:[] for i in range(1,n+1)}

        for n1,n2,t in times:
            vertMap[n1].append((n2,t))
        

        minHeap = [(0,k)]
        visited = set()
        count = 0

        while minHeap:
            w1,n1 = heapq.heappop(minHeap)

            if n1 in visited:
                continue
            
            visited.add(n1)
            count = max(count,w1)

            for n2,w2 in vertMap[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap,(w2+w1,n2))
        if len(visited) == n:
            return count
        else:
            return -1


        