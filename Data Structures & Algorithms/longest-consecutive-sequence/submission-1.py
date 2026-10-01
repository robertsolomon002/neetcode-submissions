class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        found = set()

        for i in nums:
            found.add(i)

        resp = 0


        for num in found:
            if num - 1 not in found:
                cur = 1
                while num +1 in found:
                    num = num+1
                    cur +=1
                
                resp = max(cur,resp)
        

        return resp