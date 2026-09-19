# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        slow = fast = head
        prev = []
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        temp = head
        while temp != slow:
            prev.append(temp.val)
            temp = temp.next
        if fast:
            slow = slow.next
        prev.reverse()
        i = 0
        while slow:
            if slow.val != prev[i]:
                return False
            slow = slow.next
            i += 1
        return True



        
        
        