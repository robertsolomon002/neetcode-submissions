class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for word in strs:
            length = len(word)

            res += str(length) + "|" + word
        
        return res

    def decode(self, s: str) -> List[str]:
        

        res = []
        
        i = 0

        while i < len(s):
            char = s[i]
            initial = ""
            while char != "|":
                initial += char
                print(i)
                print(initial)
                print(char)
                print("")
                i += 1
                char = s[i]
            
            initial = int(initial)

            if initial == 0:
                res.append("")
                i += 1
            
            else:

                i += 1
                char = s[i]

                next_entry = ""

                for j in range(i, i + initial):
                    next_entry += s[j]
                
                i = i + initial
                res.append(next_entry)
        return res


