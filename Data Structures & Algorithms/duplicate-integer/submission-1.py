class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map_dup = {}

        for i in range(0,len(nums)):
            if nums[i] in map_dup:
                return True
            else:
                map_dup[nums[i]] = 1
        
        return False