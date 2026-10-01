class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        res = []

        def bfs(i,k):
            if k == 0:
                res.append(curr.copy())
                return 
            
            if k < 0 or i >= len(nums):
                return
            
            curr.append(nums[i])
            bfs(i,k-nums[i])
            curr.pop()
            bfs(i+1, k)

        
        curr =[]
        bfs(0,target)

        return res