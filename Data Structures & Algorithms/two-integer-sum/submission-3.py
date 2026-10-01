class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        placement = {}

        for i,number in enumerate(nums):
            opposite = target - number

            if opposite in placement:
                j = placement[opposite]
                break
                
            elif number not in placement:
                placement[number] = i
        
        return [j,i]
        