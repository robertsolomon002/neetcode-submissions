class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        
        if len(s1) == 0:
            return True
        

        verifier = [0] * 26
        window = [0] * 26
        for i in range(len(s1)):
            verifier[ord(s1[i]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] += 1      
        
        if verifier == window:
            return True

        for i in range(1, len(s2) - len(s1) + 1):
            window[ord(s2[i-1]) - ord('a')] -=1
            window[ord(s2[i+len(s1)-1]) - ord('a')] +=1
            
            if verifier == window:
                return True
            
        print(verifier, window)

        return False

        