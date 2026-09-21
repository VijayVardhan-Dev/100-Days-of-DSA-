# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        l = 0
        tail = head

        while tail:
            tail = tail.next
            l += 1
        if l == 0:
            return head
            
        k = l - (k % l)

        if l == k:
            return head

        nb = head
        
        while k-1 > 0:
            nb = nb.next
            k -= 1 
            
        end =start= nb

        while nb.next:
            nb = nb.next

        start = start.next
        end.next = None

        nb.next = head
        return start

