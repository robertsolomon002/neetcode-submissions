from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        if k >= len(nums):
            return [max(nums)]
        if k == 0:
            return []

        if len(nums) == 0:
            return []
        my_deque = deque()
        output =[]

        i,j = 0,0
        for j in range(k):
            while my_deque and my_deque[-1] < nums[j]:
                my_deque.pop()
                
            my_deque.append(nums[j])
        
        output.append(my_deque[0])
        
        for j in range(k,len(nums)):
            print(my_deque)
            old_first = nums[i]
            if old_first == my_deque[0]:
                my_deque.popleft()
            while my_deque and my_deque[-1] < nums[j]:
                my_deque.pop()
                
            my_deque.append(nums[j])
            output.append(my_deque[0])
            i += 1




        return output


        