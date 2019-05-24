# Complexity
# Time: O(max(n, m)), where n is the size of l1 and m is the size of l2
# Space: O(max(n, m)), since I'm creating a new list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        answer = ListNode(0)
        curr_answer = answer
        
        carry_out = 0
        
        while l1 or l2 or carry_out:
            curr_val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry_out
            carry_out = curr_val//10
            curr_val %= 10
            
            curr_answer.next = ListNode(curr_val)
            curr_answer = curr_answer.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
                        
        return answer.next
