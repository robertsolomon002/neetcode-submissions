from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        t_dict = Counter(t)

        sub_s = {}
        left = 0

        need = len(t_dict)
        have =0


        best_len = float("inf")
        best_start = 0

        for right in range(len(s)):
            right_char = s[right]
            sub_s[right_char] = sub_s.get(right_char,0) + 1

            if (right_char in t_dict) and t_dict[right_char] == sub_s[right_char]:
                have +=1
            
            while have == need:
                if right - left +1 < best_len:
                    best_len = right-left+1
                    best_start = left

                sub_s[s[left]] -=1
                
                if (s[left] in t_dict) and (sub_s[s[left]] < t_dict[s[left]]):
                    have -= 1
                
                left +=1
                


        if best_len == float("inf"):
            return ""
        return s[best_start:best_start + best_len]