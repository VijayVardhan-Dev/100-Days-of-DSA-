# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        if not list1:
            return list2
        if not list2:
            return list1
        
        head = ans = ListNode()

        while list1 and list2:
            if list1.val <= list2.val:
                ans.next = list1
                ans = ans.next
                list1 = list1.next
            else:
                ans.next = list2 
                ans = ans.next
                list2 = list2.next
        ans.next = list1 or list2
        return head.next



        