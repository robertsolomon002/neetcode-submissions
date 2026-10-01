class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow_point = 0
        fast_point = 0
        while True:
            slow_point = nums[slow_point]
            fast_point = nums[fast_point]
            fast_point = nums[fast_point]
            if fast_point == slow_point:
                break


        scnd = 0

        while scnd != slow_point:
            slow_point = nums[slow_point]
            scnd = nums [scnd]
        return slow_point
        



