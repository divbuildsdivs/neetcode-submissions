# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        while head.next:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        head.next = prev
        i =0
        prev = None
        while head:
            if i == n - 1:
                if head.next:
                    head = head.next
                else:
                    return prev
            else:
                if head.next:
                    temp = head.next
                    head.next = prev
                    prev = head
                    head = temp
                else:
                    head.next = prev
                    break
            i += 1

        return head




        