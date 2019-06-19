# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq

class Wrapper:
    def __init__(self, node):
        self.node = node
        self.val = node.val
        self.next = node.next
        
    def __lt__(self, node):
        return self.val < node.val


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = filter(lambda node: True if node else False, lists)
        heap = list(map(Wrapper, heap))
        heapq.heapify(heap)
        answer = ListNode(0)
        answer_head = answer
                
        while heap:
            node = heapq.heappop(heap)
            
            if node.next:
                heapq.heappush(heap, Wrapper(node.next))
            
            answer.next = node.node
            answer = answer.next
            
        return answer_head.next