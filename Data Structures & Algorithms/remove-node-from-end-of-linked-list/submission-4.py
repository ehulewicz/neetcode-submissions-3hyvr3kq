# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = {}
        curr = head
            
        idx = 0
        while curr:
            nodes[idx] = curr
            idx += 1
            curr = curr.next

        if n == len( nodes ):
            return head.next

        remove_idx = len( nodes ) - n 
        nodes[remove_idx - 1].next = nodes[remove_idx + 1] if (remove_idx + 1) in nodes else None

        return head