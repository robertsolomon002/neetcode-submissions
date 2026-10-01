class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            local = 0

            while i != 0:
                if i % 2 ==1:
                    local+=1
                
                i = i //2
            
            res.append(local)


        return res

        