class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        counted = collections.Counter(hand)

        minHeap = []

        for key in counted:
            occ = counted[key]
            heapq.heappush(minHeap, (key,occ))

        while minHeap:
            smallest_val, numb_occ = heapq.heappop(minHeap)
            numb_occ -= 1
            local_group = []
            for i in range(1,groupSize):
                if not minHeap:
                    return False
                next_val, next_occ = heapq.heappop(minHeap)
                next_occ -=1
                if next_occ < 0 or next_val != i+smallest_val:
                    return False
                if next_occ >0:
                    local_group.append((next_val, next_occ))
            
            if numb_occ > 0:
                heapq.heappush(minHeap,(smallest_val, numb_occ))
            if local_group:
                for elem in local_group:
                    heapq.heappush(minHeap, elem)
        

        return not minHeap
        




        