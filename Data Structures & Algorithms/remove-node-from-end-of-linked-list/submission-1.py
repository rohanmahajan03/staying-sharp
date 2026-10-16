# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        new_head = ListNode(0, head)
        def removeN(head):
            nonlocal n
            if not head.next:
                return (1, head.next)
            else:
                next_count, potential_new_next = removeN(head.next)
                if next_count == n:
                    head.next = potential_new_next
                this_count = next_count + 1
                return (this_count, head.next)
        removeN(new_head)
        return new_head.next



        