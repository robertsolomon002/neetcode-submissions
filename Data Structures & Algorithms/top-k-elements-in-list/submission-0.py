class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:



        nums_freq = {}
        ranked_freq = [[] for _ in range(0,len(nums) +1)]


        for numb in nums:
            if numb not in nums_freq:
                nums_freq[numb] =0
            nums_freq[numb] += 1
        
        for keys in nums_freq:
            freq = nums_freq[keys]
            ranked_freq[freq].append(keys)
        
        result = []

        for i in range(len(ranked_freq)-1,-1,-1):
            top_freq = ranked_freq[i]

            for j in range(0,len(top_freq)):
                if len(result) == k:
                    return result
                else:
                    result.append(top_freq[j])



        return result