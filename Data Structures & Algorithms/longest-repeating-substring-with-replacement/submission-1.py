class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        char_map = {}

        left = 0
        res =0

        for right in range(len(s)):

            char_map[s[right]] = char_map.get(s[right], 0) + 1


            while (right-left+1) - max(char_map.values()) >k:
                char_map[s[left]] -=1
                left +=1

            res = max (res, right-left+1)





        return res
        