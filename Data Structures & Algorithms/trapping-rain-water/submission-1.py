class Solution:
    def trap(self, height: List[int]) -> int:

        curr_max_lef = 0
        max_left = []

        for i in range(len(height)):
            max_left.append(curr_max_lef)
            curr_max_lef = max(curr_max_lef, height[i])
        
        curr_max_r = 0
        max_r = [0] * len(height)

        for i in range(len(height)-1,-1,-1):
            max_r[i] = curr_max_r
            curr_max_r = max(curr_max_r, height[i])
        
        min_lr = [0] * len(height)

        for i in range(len(height)):
            min_lr[i] = min(max_left[i],max_r[i])
        

        total = 0

        for i in range(len(height)):
            local_water = max(0,min_lr[i] - height[i] )
            total += local_water
        
        return total