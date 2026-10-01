"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        traverse = head

        og_to_copy = {}

        while traverse:
            copy_node = Node(traverse.val)

            og_to_copy[traverse] = copy_node
            
            traverse = traverse.next
        

        returning_head = og_to_copy[head]

        second_traverse = head

        

        while second_traverse:
            copy_node = og_to_copy[second_traverse]

            og_next = second_traverse.next
            copy_next = None
            
            og_rand = second_traverse.random
            copy_ran = None


            if og_next:
                copy_next = og_to_copy[og_next]

            if og_rand:
                copy_ran = og_to_copy[og_rand]

            copy_node.next = copy_next
            copy_node.random =copy_ran

            second_traverse = second_traverse.next





        return returning_head

        