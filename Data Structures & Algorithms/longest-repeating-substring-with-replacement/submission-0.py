class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0 

        char_map = {}

        max_len = 0
        

        for j in range(len(s)):
            max_same_char =0
            new_char = s[j]
            if new_char not in char_map:
                char_map[new_char] = 0
            char_map[new_char] += 1
            
            for p in char_map:
                max_same_char = max(max_same_char, char_map[p])
            
            str_len = j-i+1
            if (str_len - max_same_char ) > k:
                char_map[s[i]] -= 1
                i += 1
            
            
            max_len = max(max_len, j-i+1)

            



        return max_len