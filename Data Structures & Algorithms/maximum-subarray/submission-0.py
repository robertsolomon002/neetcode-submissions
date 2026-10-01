class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        current_max = nums[0]


        prescript_sum = 0


        for j in range(len(nums)):
            curr_val = nums[j]

            if prescript_sum < 0:
                prescript_sum = 0
            prescript_sum += curr_val


            current_max = max(current_max, prescript_sum)

        return current_max





