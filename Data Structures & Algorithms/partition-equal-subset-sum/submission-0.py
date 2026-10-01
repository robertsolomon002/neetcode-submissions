class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        n = len(nums)
        total = sum(nums)

        if total % 2 == 1:
            return False
        half = int(total/2)

        dp = [False] * (half+1)
        dp[0] = True

        for num in nums:
            for j in range(half, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        return dp[half]