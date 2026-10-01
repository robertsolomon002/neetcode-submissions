class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        n = len(s)


        if len(t) != n:
            return False



        s_anagram = {}
        unique = 0

        for i in range(0,n):
            letter = s[i]
            
            if letter not in s_anagram:
                s_anagram[letter] = 0
                unique += 1
            

            s_anagram[letter] += 1

        
        count = 0
        print(s_anagram)
        for i in range(0,n):
            letter = t[i]

            if letter not in s_anagram:
                return False
            
            l_count = s_anagram[letter]

            if l_count == 0:
                return False

            else:
                s_anagram[letter] -= 1

                if s_anagram[letter] == 0:
                    count +=1
        
        print(s_anagram)
        print(count)
        return count == unique


