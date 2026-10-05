# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        mid = head
        last = head

        while last.next and last.next.next:
            mid = mid.next
            last = last.next.next
        
        if last.next:
            last = last.next

        node = mid.next
        mid.next = None
        prev = None
        
        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp

        head1=head
        
        while prev:
            temp = head1.next
            head1.next = prev
            prev_next = prev.next
            prev.next = temp

            head1 = temp
            prev = prev_next


        