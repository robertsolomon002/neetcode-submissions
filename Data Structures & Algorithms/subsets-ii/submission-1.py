class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        output = []
        local = []

        def dfs(i):
            if i >= len(nums):
                output.append(local.copy())
                return
            
            number = nums[i]

            local.append(number)
            dfs(i+1)

            local.pop()

            j = i
            while j < len(nums)-1 and nums[j+1] == nums[j]:
                j +=1
            dfs(j+1)




        dfs(0)
        return output
        