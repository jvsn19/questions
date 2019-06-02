# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p_a = head
        new_head = ListNode(0)
        new_head.next = head
        p_b = new_head
        
        for _ in range(n):
            p_a = p_a.next
            
        while p_a:
            p_a = p_a.next
            p_b = p_b.next
            
        
        p_b.next = p_b.next.next
        return new_head.next
