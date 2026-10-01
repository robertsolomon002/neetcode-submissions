class Solution:
    def minWindow(self, s: str, t: str) -> str:

        t_dict = {}

        for c in t:
            if c not in t_dict:
                t_dict[c] = 0
            t_dict[c] += 1
        
        res = ""
        j = 0
        sub_count = {}
        numb_let = 0

        for i,char in enumerate(s):
            if char in t_dict:
                if char not in sub_count:
                    sub_count[char] = 0
                sub_count[char] += 1
                if sub_count[char] == t_dict[char]:
                    numb_let += 1
                    print(char)
                    print(sub_count)
                    print(t_dict)
                    print(numb_let)
                    
                if numb_let == len(t_dict):

                    while True:
                        charj = s[j]
                        if charj not in t_dict:
                            j += 1
                        elif sub_count[charj] > t_dict[charj]:
                            sub_count[charj] -= 1
                            j +=1
                        else:
                            break
                    
                    new_len = i-j +1
                    if new_len < len(res) or res == "":
                        res = s[j:i+1]
                        print(sub_count)
                        print(t_dict)
        


        
        return res




        