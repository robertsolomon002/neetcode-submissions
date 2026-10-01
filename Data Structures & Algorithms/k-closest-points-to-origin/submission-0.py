import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k == 0:
            return []

        maxHeap = []

        for i in range(len(points)):
            coord = points[i]
            x_coord = coord[0]
            y_coord = coord[1]
            dist = math.sqrt(x_coord**2 + y_coord**2)

            if len(maxHeap) < k:
                heapq.heappush(maxHeap, (-dist,coord))
            else:
                top_dist = -1 * maxHeap[0][0]
                #print(top_dist)

                if dist < top_dist:
                    heapq.heappop(maxHeap)
                    heapq.heappush(maxHeap, (-dist,coord))
        
        result = []

        for dist,coord in maxHeap:
            result.append(coord)
        
        return result



        