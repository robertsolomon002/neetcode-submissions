class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_dict = {}

        for word in strs:
            counts = [0] * 26
            for letter in word:
                counts[ord(letter) - ord('a')] += 1

            key = tuple(counts)

            if key not in anagram_dict:
                anagram_dict[key] = []
            anagram_dict[key].append(word)
        
        return list(anagram_dict.values())
        