# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        tail = head
        count = 0
        while tail :
            count += 1
            tail = tail.next

        if count == n:
            return head.next

        tail = head
        i = 1
        while tail and i < count - n:
            tail = tail.next
            i += 1
        
        tail.next = tail.next.next

        return head
        
        