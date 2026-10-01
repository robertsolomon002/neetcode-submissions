class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        if len(s) == 0:
            return[]

        char_map = {}

        for i,char in enumerate(s):
            char_map[char] = i
        

        left = 0

        right = char_map[s[0]]

        result = []
        for i in range(len(s)):
            print(i)
            print(right)
            curr_char = s[i]
            if char_map[curr_char] > right:
                right = char_map[curr_char]
            
            if i == right:
                result.append(right - left +1)
                if i != len(s)-1:
                    left = i + 1
                    right = char_map[s[left]]
        
        return result