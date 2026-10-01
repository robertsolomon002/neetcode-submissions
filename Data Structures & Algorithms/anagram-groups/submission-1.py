class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}


        for w in strs:
            local = [0] * 26
            for c in w:
                local[ord(c) - ord("a")] += 1
            
            search = tuple(local)

            if search not in anagrams:
                anagrams[search] = []
            
            anagrams[search].append(w)
        print(anagrams.values())
        return list(anagrams.values())

        