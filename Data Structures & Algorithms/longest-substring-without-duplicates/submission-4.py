class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        max_len = 0
        dict_char ={}
        for j in range(len(s)):
            new_char = s[j]
            #if j ==0:
            #    dict_char[new_char] = j
            #    max_len = 1
            #else:
            if new_char not in dict_char:
                dict_char[new_char] = j
                max_len = max(max_len, j-i +1)
            else:
                pos_new_char = dict_char[new_char]
                if i <= pos_new_char:
                    i = pos_new_char +1
                dict_char[new_char] = j
                max_len = max(max_len, j-i +1)



        
        return max_len
        