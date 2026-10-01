class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numb = set()

        for ints in nums:
            numb.add(ints)
        
        #print(numb)
        longest_seq = 0
        for ints in nums:
            if (ints -1) not in nums:
                #print(ints)
                start = ints
                end = ints
                while end +1 in nums:
                    end +=1
                
                longest_seq = max(longest_seq, end-start +1)
        return longest_seq

        
        