class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        numb_to_freq = {}
        freq_to_numb = {}


        for number in nums:
            numb_to_freq[number] = numb_to_freq.get(number,0) + 1
            
        max_freq = 0

        for number,freq in numb_to_freq.items():
            freq_to_numb.setdefault(freq,[]).append(number)
            if freq > max_freq:
                max_freq = freq

        result = []

        for i in range(max_freq,0,-1):
            numb_of_freq_i = freq_to_numb.get(i,[])

            for number in numb_of_freq_i:
                result.append(number)
                if len(result) == k:
                    return result

