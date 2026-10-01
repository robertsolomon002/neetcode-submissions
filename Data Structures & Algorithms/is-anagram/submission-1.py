class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    
        s_gram = {}


        for w in s:
            if w not in s_gram:
                s_gram[w] = 0
            s_gram[w] +=1
        
        same = 0

        for l in t:
            if (l not in s_gram) or s_gram[l] == 0:
                return False
            
            s_gram[l] -= 1

            if s_gram[l] == 0:
                same += 1
        

        return same == len(s_gram)

            