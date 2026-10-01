# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return None
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        

        #if fast == None -> Uneven (so slow is mid), else

        prev = None
        curr = slow.next

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        slow.next = None

        curr_left = head
        curr_right = prev

        while curr_right:
            next_curr_left = curr_left.next
            next_curr_right = curr_right.next

            curr_left.next = curr_right
            curr_right.next = next_curr_left

            curr_left = next_curr_left
            curr_right =next_curr_right










        