class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        j=0

        tracker = {}

        for i,c in enumerate(s):
            print(j)
            if c not in tracker:
                tracker[c] = i
            else:
                last_time = tracker[c]
                tracker[c] = i
                if last_time >= j:
                    j = last_time + 1
            res = max(res, i-j +1)
        print(tracker)
        print(j)

            



        return res
        