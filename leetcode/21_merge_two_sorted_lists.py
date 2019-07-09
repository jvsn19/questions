class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        answer = ListNode(0)
        head = answer
        
        while l1 or l2:
            
            if l1 and l2:
                if l1.val > l2.val:
                    answer.next = ListNode(l2.val)
                    l2 = l2.next
                    
                else:
                    answer.next = ListNode(l1.val)
                    l1 = l1.next
                    
                answer = answer.next
                
            else:
                if l1: answer.next = l1
                else: answer.next = l2
                break
                
        return head.next