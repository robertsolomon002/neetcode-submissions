class Solution:
    def maxArea(self, heights: List[int]) -> int:

        res =0


        left = 0
        right = len(heights) -1

        while left < right:
            cur_vol = (right - left) * min(heights[right],heights[left])

            res = max(cur_vol,res)

            if heights[right] < heights[left]:
                right -=1
            else:
                left += 1







        return res
        