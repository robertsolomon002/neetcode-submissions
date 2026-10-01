class Solution:
    def climbStairs(self, n: int) -> int:
        if n==0 or n==1:
            return 1
        one = 1
        two = 1

        for i in range(n-2):
            old_two = two
            two = one+ two
            one = old_two
        
        return two+one

        