# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:



        dummy = ListNode(0,head)
        groupPrev = dummy 

        while True:
            k_node = self.getKth(groupPrev, k)
            if not k_node:
                break
            groupNext = k_node.next

            prev, curr = k_node.next  , groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            tmp = groupPrev.next
            groupPrev.next = k_node
            groupPrev = tmp

        return dummy.next


            

    

    def getKth(self, head, k):
        curr = head

        while curr and k >0:
            curr = curr.next
            k -= 1

        
        return curr