class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []

        def dfs(i,cur, total):
            if total == target:
                res.append(cur.copy())
                return 
            if i >= len(nums) or total > target:
                return
            curr_number = nums[i]

            cur.append(curr_number)
            dfs(i, cur, total + curr_number)

            cur.pop()
            dfs(i+1, cur, total)

        dfs(0,[],0)

        return res



        