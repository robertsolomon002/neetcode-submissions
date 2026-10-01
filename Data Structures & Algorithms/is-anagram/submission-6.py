class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first_word = {}

        for letter in s:
            if letter not in first_word:
                first_word[letter] = 0
            first_word[letter] += 1
        
        for letter in t:
            if letter not in first_word:
                return False
            else:
                first_word[letter] -=1
                if first_word[letter] == 0:
                    del first_word[letter]
        
        return not first_word
        