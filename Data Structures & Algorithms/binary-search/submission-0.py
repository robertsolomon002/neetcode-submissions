class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) -1

        while i <= j:
            mid = int( (i + j) / 2)
            mid_val = nums[mid]
            print("")
            print(mid)
            print(mid_val)
            if mid_val == target:
                return mid
            elif mid_val < target:
                i = mid + 1
            else:
                j = mid -1        
        return -1

        