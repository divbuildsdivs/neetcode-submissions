# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minheap = []
        heapq.heapify(minheap)
        for i in range(len(lists)):
            head = lists[i]
            while head:
                heapq.heappush(minheap,head.val)
                head = head.next
        head = ListNode(None)
        dummy = head
        while minheap:
            node = ListNode(heapq.heappop(minheap))
            dummy.next = node
            dummy = dummy.next
        
        return head.next
        