class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checker = {}

        for number in nums:
            if number in checker:
                return True
            else:
                checker[number] = 1
            
        return False


        