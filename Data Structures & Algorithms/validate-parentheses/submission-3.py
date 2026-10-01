class Solution:
    def isValid(self, s: str) -> bool:

        open_stack =[]

        open_par = {'(':')','[':']', '{':'}'}

        for i in range(len(s)):
            char = s[i]
            if char in open_par:
                open_stack.append(char)
            else:
                if open_stack:
                    prev_close = open_stack.pop()

                    if open_par[prev_close] != char:
                        return False

                else:
                    return False

        return not open_stack