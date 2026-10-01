class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        if len(stones) == 0:
            return 0
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)

        while len(stones) > 1:
            first_rock = -1 * heapq.heappop(stones)
            second_rock = -1 * heapq.heappop(stones)   

            result_rock = -(first_rock - second_rock)

            heapq.heappush(stones, result_rock)
        


        return -stones[0]