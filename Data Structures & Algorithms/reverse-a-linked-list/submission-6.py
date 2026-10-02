# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        past = None
        node = head

        while node:
            temp_next = node.next
            node.next = past

            past = node
            node = temp_next
        
        return past
        