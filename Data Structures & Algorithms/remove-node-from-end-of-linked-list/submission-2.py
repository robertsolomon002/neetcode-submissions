# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        length = 0
        pointer = head

        while pointer:
            length +=1
            pointer = pointer.next
        
        index = length - n

        if index ==0:
            head = head.next
            return head
        
        prev = head
        rem = head.next

        traverse = 1

        while index != traverse:
            prev = rem
            rem = rem.next
            traverse +=1
        prev.next = rem.next
        return head
        