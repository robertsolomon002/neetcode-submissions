class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) -1

        if nums[i] <= nums[j]:
            return nums[i]
        
        while (i <= j):
            mid = (i+j)//2
            val_mid = nums[mid]
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]

            elif nums[mid] >= nums[i]:
                i = mid +1
            else:
                j = mid -1

        return -1