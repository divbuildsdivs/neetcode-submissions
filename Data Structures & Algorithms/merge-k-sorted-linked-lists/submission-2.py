# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        if k == 0:
            return None
        elif k == 1:
            return lists[0]
        elif k == 2:
            return self.merge2Lists(lists[0], lists[1])
        mergedLists = []
        for i in range(0, k, 2):
            if i+1 < k:
                mergedLists.append(self.merge2Lists(lists[i], lists[i+1]))
            else:
                mergedLists.append(lists[i])
        return self.mergeKLists(mergedLists)
            
        
    def merge2Lists(self, list1, list2):
            head = ListNode(None)
            dummy = head
            while list1 and list2:
                if list1.val < list2.val:
                    dummy.next = list1
                    list1 = list1.next
                else:
                    dummy.next = list2
                    list2 = list2.next
                dummy = dummy.next
            if list1:
                dummy.next = list1
            elif list2:
                dummy.next = list2
            return head.next

        

        