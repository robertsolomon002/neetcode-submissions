class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        current = []


        def backtract(i):

            #print(i)
            if i >= len(nums):
                print(current)
                res.append(current.copy())
                return
           # print(i)
            current.append(nums[i])
            backtract(i+1)
            current.pop()
           # print("AAAAA"            )
            #print(current)
            #print(i)
            #print("AAAA")
            backtract(i+1)
        backtract(0)





        return res
        