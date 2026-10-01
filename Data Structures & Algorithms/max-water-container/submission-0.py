class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        max_v = 0
        while i< j:
            curr_h = min(heights[i],heights[j])
            curr_v = curr_h * (j-i)
            max_v = max(curr_v, max_v)

            if curr_h == heights[i]:
                i += 1
            else:
                j -=1


        return max_v
        