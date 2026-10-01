class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0

        jump_len = 0

        jump_start = 0

        for i in range(len(nums)-1):
            jump_len = max(jump_len, i + nums[i])

            if i == jump_start:
                jumps += 1
                jump_start = jump_len


        return jumps
            
        