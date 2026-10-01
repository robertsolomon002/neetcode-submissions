class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        

        result =[]

        combination = []
        def dfs(i):
            if i >= len(digits):
                result.append("".join(combination))
                return
            int_dig = int(digits[i])


            if int_dig in range(2,8):
                start = (int_dig -2) * 3
            else:
                start = (int_dig -2) * 3 +1
            len_loop = 3
            if int_dig == 7 or int_dig == 9:
                len_loop +=1
            print(int_dig)
            for j in range(len_loop):
                print(start,j)
                char = chr(ord("a") + start + j)
                combination.append(char)
                print(char)
                dfs(i+1)
                print(combination)
                combination.pop()






        dfs(0)
        return result