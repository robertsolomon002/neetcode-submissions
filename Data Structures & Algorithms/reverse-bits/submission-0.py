class Solution:
    def reverseBits(self, n: int) -> int:

        bin_list = 0

        for i in range(31, -1,-1):
            if n % 2 == 1:
                print(2**i)
                print(i)
                bin_list += 2 **i

            n = n //2

        return bin_list
        