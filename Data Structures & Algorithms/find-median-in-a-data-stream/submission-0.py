class MedianFinder:

    def __init__(self):
        #min heap of all top elem
        self.topHeap = []

        #max heap of all bot elem
        self.botHeap = []
        

    def addNum(self, num: int) -> None:

        heapq.heappush(self.botHeap,  -num)

        if (self.topHeap and self.botHeap and
            (-1 * self.botHeap[0]) > self.topHeap[0]):
            heapq.heappush(self.topHeap, -heapq.heappop(self.botHeap))

        if len(self.botHeap) > len(self.topHeap) + 1:

            largest_small_val = - heapq.heappop(self.botHeap)

            heapq.heappush(self.topHeap, largest_small_val)
        if len(self.topHeap) > len(self.botHeap) +1 :
            smallest_large_val = heapq.heappop(self.topHeap)

            heapq.heappush(self.botHeap, -smallest_large_val)

        


                
        

    def findMedian(self) -> float:
        if len(self.botHeap) > len(self.topHeap):
            return -self.botHeap[0]

        if len(self.topHeap) > len(self.botHeap):
            return self.topHeap[0]
        
        return ((-self.botHeap[0] + self.topHeap[0]) /2)
        
        