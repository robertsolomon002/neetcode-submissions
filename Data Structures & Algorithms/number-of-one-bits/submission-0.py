class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        print(n)

        while n != 0:
            if n % 2 == 1:
                count += 1
            n = n //2
        return count
