import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if not piles:
            return 0

        left = 1
        right = max(piles)
        best = right

        while left <= right:
            mid = (left + right) // 2
            total_hours = sum(math.ceil(p / mid) for p in piles)

            if total_hours <= h:
                best = mid
                right = mid - 1  # try to find smaller k
            else:
                left = mid + 1   # need faster speed

        return best
            



        return recent