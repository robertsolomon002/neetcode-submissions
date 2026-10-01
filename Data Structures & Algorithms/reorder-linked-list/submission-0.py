# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        curr = head
        go_end = True
        while curr and curr.next:
            print(curr.val)
            ending = curr
            if go_end:
                prev_end = None
                while ending.next:
                    prev_end = ending
                    ending = ending.next
                if curr == ending or curr.next == ending:
                    break

                prev_end.next =None
                split = curr.next

                curr.next = ending
                ending.next = split
                curr = curr.next
                go_end = False
            else:
                curr = curr.next
                go_end = True


        