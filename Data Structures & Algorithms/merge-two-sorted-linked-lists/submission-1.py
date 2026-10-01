# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1:
            return list2
        if not list2:
            return list1


        head = list1
        if list2.val < list1.val:
            head = list2
            list2 = list2.next
        else:
            list1 = list1.next

        curr = head

        while list1 and list2:
            next_node = list1
            if list2.val < list1.val:
                next_node = list2
                list2 = list2.next
            else:
                list1=list1.next
            
            curr.next = next_node
            curr = next_node
        
        if not list1:
            curr.next = list2
        elif not list2:
            curr.next =list1

        return head

        