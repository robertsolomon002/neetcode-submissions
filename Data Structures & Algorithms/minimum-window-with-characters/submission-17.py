class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        if len(t) == 0:
            return ""
        template_dict = {}
        our_word_dict = {}

        for i,text in enumerate(t):
            if text not in template_dict:
                template_dict[text]=0
                our_word_dict[text] = 0
            template_dict[text] += 1

        for i in range(len(t)):
            char = s[i]
            if char in our_word_dict:
                our_word_dict[char] += 1
        
        matches = 0


        for word in t:
            if template_dict[word] <= our_word_dict[word]:
                matches += 1
        #print(template_dict,our_word_dict )
        if matches == len(t): return s[:len(t)]
        start = -1
        end = -1
        i= 0
        for j in range(len(t),len(s)):
            #print(matches)
            
            new_char = s[j]
            #print(new_char)
            if new_char in template_dict: 
                if our_word_dict[new_char] >= template_dict[new_char]:
                    our_word_dict[new_char] += 1
                    
                else:
                    our_word_dict[new_char] += 1
                    print(our_word_dict)
                    print(template_dict)
                    if our_word_dict[new_char] >= template_dict[new_char]:
                        print("MATCH")
                        matches += 1
                        print(matches)
                        print("------")
                        if matches == len(template_dict):
                            print("---------")
                            print("MATCH FOUND")
                            print(i,j)
                            if (j-i +1 ) < (end - start+ 1) or start ==- 1:
                                end = j
                                start = i
                            while matches == len(template_dict):
                                print(i)
                                rem_w = s[i]
                                i += 1
                                if rem_w in our_word_dict:
                                    our_word_dict[rem_w] -= 1
                                    if our_word_dict[rem_w] < template_dict[rem_w]:
                                        print("We got new interval and new end/start")
                                        print(i,j)
                                        print(end,start)
                                        matches -= 1
                                    else:
                                        if (j-i +1 ) < (end - start+ 1) or start ==- 1:
                                            end = j
                                            start = i
                                else:
                                    if (j-i +1 ) < (end - start+ 1) or start ==- 1:
                                        end = j
                                        start = i
        print(our_word_dict)
        print(template_dict)
        if start == -1:
            print("no match ever found")
            return ""
        else:
            return s[start:end+1]

