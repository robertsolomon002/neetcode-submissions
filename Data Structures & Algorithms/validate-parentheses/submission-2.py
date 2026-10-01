class Solution:
    def isValid(self, s: str) -> bool:

        stacks = []

        open_brack = {"(": ")", "{" :"}", "[" : "]"}

        for char in s:
            if char in open_brack:
                stacks.append(char)
            else:
                if stacks == []:
                    return False
                complement = stacks.pop()
                if open_brack[complement] != char:
                    return False
        
        return stacks == []
                



        