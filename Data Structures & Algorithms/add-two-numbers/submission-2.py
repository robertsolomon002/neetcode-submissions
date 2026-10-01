# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        curr = dummy

        carry = False


        while l1 or l2:
            l1_val = 0
            if l1:
                l1_val = l1.val
            l2_val = 0
            if l2:
                l2_val = l2.val
            

            total = l1_val + l2_val

            if carry == True:
                total +=1
                carry = False

            if total > 9:
                carry = True
                total = total % 10
            curr.next = ListNode(total)

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            curr = curr.next
        if carry:
            curr.next = ListNode(1)





        return dummy.next
        