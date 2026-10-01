
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k ==0:
            return []
        numsfreq = {}

        for n in nums:
            if n not in numsfreq:
                numsfreq[n] = 0
            numsfreq[n] += 1
        
        n = len(nums)
        k_freq = {i: [] for i in range(0,n+1)}

        for key in numsfreq:
            freq = numsfreq[key]
            k_freq[freq].append(key)
        
        res = []

        print(k_freq)
        for j in range(n,-1,-1):
            k_list = k_freq[j]
            print(k_list)
            for h in k_list:

                res.append(h)                
                if len(res) == k:
                    return res
        print(res)


        