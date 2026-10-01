class Solution:
    def countSubstrings(self, s: str) -> int:
        numb = 0


        for i in range(len(s)):

            #odd pals

            left,right = i,i

            while left >= 0 and right <= len(s) -1 and s[left] == s[right]:
                numb += 1
                left -= 1
                right += 1
            
            left,right = i, i +1
            while left >= 0 and right <= len(s) -1 and s[left] == s[right]:
                numb += 1
                left -= 1
                right += 1


            #even pals





        return numb
        