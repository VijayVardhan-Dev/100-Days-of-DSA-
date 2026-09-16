# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return head
        slow = fast = head
        while fast.next:
            if fast.next.val != slow.val:
                slow.next = fast.next
                slow = slow.next
                fast = fast.next
            else:
                while fast.next and fast.next.val == slow.val:
                    fast = fast.next
        slow.next = None
        return head