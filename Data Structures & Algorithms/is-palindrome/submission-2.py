class Solution:
    def isPalindrome(self, s: str) -> bool:

        length = len(s)


        left = 0
        right = length -1



        while left < right:

            while left < right and not s[left].isalnum():
                left +=1
            while left <right and not s[right].isalnum():
                right -=1

            left_char = s[left].lower()
            right_char = s[right].lower()


            if left_char != right_char:
                return False



            left +=1
            right -=1

        
        return True