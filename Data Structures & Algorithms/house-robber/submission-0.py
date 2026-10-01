class Solution:
    def rob(self, nums: List[int]) -> int:


        for i in range(len(nums)):
            if i-2< 0:
                two_left = 0
            else:
                two_left = nums[i-2]
            
            if i - 1<0:
                one_left = 0
            else:
                one_left = nums[i-1]
            nums[i] = max(nums[i] + two_left, one_left)
        
        print(nums)
        return nums[-1]