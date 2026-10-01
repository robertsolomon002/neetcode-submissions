class Solution:
    def search(self, nums: List[int], target: int) -> int:

        i = 0
        j = len(nums) -1


        while i <= j:
            mid = (i+j)//2
            mid_val = nums[mid]
            print("-----"
            )
            print(i)
            print(j)
            print(mid_val)
            if mid_val == target:
                return mid
            if nums[i] == target:
                return i
            if nums[j] == target:
                return j
            if mid_val >= nums[i]:
                if target > mid_val or target <= nums[i]:
                    i = mid + 1
                else:
                    j = mid -1

            else:
                if target < mid_val or target >= nums[j]:
                    j = mid -1
                else:
                    i = mid+1



        print("====")
        print(i)
        print(j)

        return -1
        