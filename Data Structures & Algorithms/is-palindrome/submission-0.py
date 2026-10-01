class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        i = 0
        j = len(s) -1
        while i < j:
            while not s[i].isalnum():
                i += 1
                if i >= len(s):
                    return True
            while not s[j].isalnum():
                j -= 1

            #print(s[i])
            #print(s[j])
            
            if s[i] != s[j]:
                return False
            else:
                i+=1
                j-=1
            
        

        return True
        