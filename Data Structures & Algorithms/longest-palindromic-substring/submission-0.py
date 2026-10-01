class Solution:
    def longestPalindrome(self, s: str) -> str:

        res = ""
        resLen = 0

        for i in range(len(s)) :
            #odd
            left,right = i,i

            while left >= 0 and right <= len(s) -1:
                if s[left] != s[right]:
                    break
                if right - left +1 > resLen:

                    resLen = right - left +1
                    res = s[left:right +1]
                left -= 1
                right +=1


            #evn
            left,right = i,i +1

            while left >= 0 and right <= len(s) -1:
                if s[left] != s[right]:
                    break
                if right - left +1 > resLen:

                    resLen = right - left +1
                    res = s[left:right +1]
                left -= 1
                right +=1





        return res
        