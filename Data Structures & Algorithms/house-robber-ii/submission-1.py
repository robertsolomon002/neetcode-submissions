class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) ==1:
            return nums[0]
        first_half = nums[:len(nums)-1].copy()
        second_half = nums[1:].copy()
        for i in range(len(first_half)):
            if i-2 <0:
                two = 0
            else:
                two = first_half[i-2]
            
            if i-1<0:
                one = 0
            else:
                one = first_half[i-1]

            first_half[i] = max(first_half[i] + two, one)

        for i in range(len(second_half)):
            if i-2 <0:
                two = 0
            else:
                two = second_half[i-2]
            
            if i-1<0:
                one = 0
            else:
                one = second_half[i-1]

            second_half[i] = max(second_half[i] + two, one)
        return max(second_half[len(second_half)-1],first_half[len(first_half)-1])
        
        