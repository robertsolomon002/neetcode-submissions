class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        complement_map = {}
        
        for i in range(0,len(nums)):
            complement = target - nums[i]

            if complement in complement_map:
                return [complement_map[complement], i]
            else:
                complement_map[nums[i]] = i